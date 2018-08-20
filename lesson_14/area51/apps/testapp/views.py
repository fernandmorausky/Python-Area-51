from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from apps.testapp.models import Developer
import datetime


def root(request):
    # assert False  # Sirve para romper el flujo
    return HttpResponse('Area 51 Training Center')


def hello(request):
    return HttpResponse('Hello World!')


def current_time(request):
    print(dir(request))  # Muestra en consola
    now = datetime.datetime.now()

    html = '''
    <html>
        <body>
            <h1>TEST: Hora Actual</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(now)

    return HttpResponse(html)


def time_ahead(request, ahead):
    now = datetime.datetime.now()
    time = now + datetime.timedelta(hours=int(ahead))
    html = '''
    <html>
        <body>
            <h1>TEST: Agregar {} hora(s)</h1>
            <h3>{}</h3>
        </body>
    </html>
    '''.format(ahead, time)
    return HttpResponse(html)


def create_dev(request, username):
    lastname = username[::-1]
    email = '{}@area51.pe'.format(username)
    dev = Developer.objects.create(name=username, lastname=lastname, email=email)
    #dev = Developer(name=username, lastname=lastname, email=email)
    #dev.save()
    return HttpResponse('Created Developer')


def devs(request):
    devs = Developer.objects.all()
    s = ''
    for dev in devs:
        s += '{} '.format(dev.name)
    return HttpResponse(s)


def devs_template(request):
    devs = Developer.objects.all()
    context = {'devs': devs}
    return render(request, 'testapp.html', context)

