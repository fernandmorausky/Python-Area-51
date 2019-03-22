import json
import datetime
import requests
from django.shortcuts import render , redirect
from django.http import HttpResponse
from apps.repository.models import Repository
# Create your views here.
def index(request):
    return redirect('1/')


def list_repository(request, sorted='1'):
    #
    if(sorted == '1'):
        sorted = 'created'
    elif(sorted == '2'):
        sorted = 'pushed'

    repos = get_repos_github(sorted)
    
    save_data(repos)

    repos = {'repos' : repos}

    return render(request, 'repository/index.html', repos)

def get_repos_github(sort='created'):
    url = 'https://api.github.com/users/githubtraining/repos'
    params = {
        'sort': sort
    }
    r = requests.get(url=url, params=params)
    return r.json()

def save_data(repos):
    for repo in repos:
        print(repo)
        print(datetime.datetime.now())
        rep = Repository.objects.filter(id=repo.id)
        print(rep)
        if(rep):
            rep.LastConsultation=datetime.datetime.now()
        else:
            rep = Repository(id=repo.id, Name=repo.name, LastCommit=repo.pushed_at, LastConsultation=datetime.datetime.now())
        rep.save()
