from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import userdata

from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def login(request):
    return render(request, 'login.html')


def dino(request):
    return render(request, 'dino.html')

def game(request):
    return render(request, 'missile.html')

def coil(request):
    return render(request, 'coil.html')

def tzfe(requests):
    return render(requests, 'tzfe.html')

def gravity(request):
    return render(request, 'game.html')

def mario(request):
    return render(request, 'mario.html')

def signup(request):
    return render(request, 'signup.html')

def saveuser(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pas = request.POST.get('password')
        da = userdata(user=user, password=pas)
        da.save()
    count = dir(userdata)
    nxt = userdata.objects.all()
    all_user=''
    for i in nxt:
        all_user += ' '+i.user
        if i.user == 'vishal':
            exi = 'user found'
            break
        else:
            exi = 'user not found'
    context = {
        'user_count' : count,
        'nxt_data' : nxt,
        'exi' : exi,
    }
    return render(request, 'saveuser.html', context=context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pas = request.POST.get('pas')
        user = authenticate(username=username, password=pas)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'todo.html', None)
        else:
            return render(request, 'wp.html', None)
