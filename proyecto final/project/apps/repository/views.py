import json
import datetime
import requests
from django.contrib import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse
from apps.repository.models import Repository
# Create your views here.
def index(request):
    return redirect('/repo/index/1/')


def list_repository(request, sorted='1'):
    if(sorted == '1'):
        sorted = 'created'
    elif(sorted == '2'):
        sorted = 'pushed'
    if request.session.has_key('grepos') and request.session.has_key('sorted') and request.session['sorted'] == sorted:
        repos = request.session['grepos']
    else:
        repos = get_repos_github(sorted)
        save_data(repos)
        request.session['grepos'] = repos
        request.session['sorted'] = sorted
    repos = {'repos' : repos}
    return render(request, 'repository/index.html', repos)


def get_repos_github(sort='created'):
    url = 'https://api.github.com/users/githubtraining/repos'
    params = {
        'sort': sort
    }
    r = requests.get(url=url, params=params)
    return r.json()


def sarch_repo(request):
    if request.session.has_key('grepos'):
        grepos = request.session['grepos']
        if 'name' in request.GET and request.GET['name']:
            name = request.GET['name']
            repo = [ d  for d in grepos if d.get('name') == name]
            if repo:
                repos_aux = repo
                save_data(repos_aux)
            else:
                repos_aux = grepos
                messages.info(request, 'No se encontro repositorio.')
        else:
            repos_aux = grepos
            messages.info(request, 'Ingrese nombre de repositorio!.')
    else:
        return redirect('/repo/index/1/')
    
    repos = { 'repos' : repos_aux }
    return render(request, 'repository/index.html', repos)


def save_data(repos):
    if len(repos) > 10:
        repos_to_save = repos[-10::]
    else:
        repos_to_save = repos

    for repo in repos_to_save:
        print(repo.get('id'))
        rep = Repository.objects.filter(id=repo.get('id')).first()
        if rep:
            rep.LastConsultation=datetime.datetime.now()
        else:
            rep = Repository(id=repo.get('id'), Name=repo.get('name'), LastCommit=repo.get('pushed_at'), LastConsultation=datetime.datetime.now())
        rep.save()
