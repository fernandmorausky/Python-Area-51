# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json

date = '25/12/2017'
body = {
    'TIP_Consulta': '2',
    'TIP_Lengueta': 'tdDos',
    'TIP_Causa': 'C',
    'ROL_Causa': '',
    'ERA_Causa': '',
    'FEC_Desde': date,
    'FEC_Hasta': date,
    'RUT_Consulta': '',
    'RUT_DvConsulta': '',
    'NOM_Consulta': '',
    'APE_Paterno': '',
    'APE_Materno': '',
    'COD_Tribunal': '0',
    'irAccionAtPublico': 'Consulta'
}

url_1 = 'https://civil.pjud.cl/CIVILPORWEB/AtPublicoDAction.do'
url_2 = 'https://civil.pjud.cl'

sess = requests.Session()
y = sess.get('https://civil.pjud.cl/CIVILPORWEB/')
r = sess.get('https://civil.pjud.cl/CIVILPORWEB/AtPublicoViewAccion.do?tipoMenuATP=1')

print(r)
print(r.history)
print(r.status_code)
print(dir(r))
r = sess.post(url_1, data=body)

print(r)
print(r.history)
print(r.status_code)
print(dir(r))

soup = BeautifulSoup(r.text, "lxml")

print()
print("contentCellsAddTabla")
soup2=soup.find('table',{"id":"contentCellsAddTabla"})
print(type(soup))
print(type(soup2))

fields = []
print(soup2.tbody.find_all('tr')[0].find_all('td')[0])
for child in soup2.tbody.find_all('tr'):
    cols=child.find_all('td')
    
    link=cols[0].a['href']
    rol=cols[0].text.strip()
    date=cols[1].text.strip()
    judge=cols[3].text.strip()
    litigants=[]

    html_2 = requests.get(url_2 + link).text
    soup3 = BeautifulSoup(html_2, "lxml")
    for l in soup3.find('div',{"id":"Litigantes"}).find_all('tr',{"class":["lineaGrilla1","lineaGrilla2"]}):
        cols2=l.find_all('td')
        litigant = {'participante': cols2[0].text.strip(), 'rut': cols2[1].text.strip().split('-')[0], 
        'dv': cols2[1].text.strip().split('-')[1], 'persona': cols2[2].text.strip(), 'nombre': cols2[3].text.strip()}
        litigants.append(litigant)
    print(litigants)
    d = {'rol': rol, 'tribunal': judge, 'fecha_ingreso': date, 'litigantes': litigants}
    fields.append(d)

print(fields)