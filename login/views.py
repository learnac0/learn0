from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import userdata
# Create your views here.
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
        user = request.POST.get('user')
        pas = request.POST.get('password')
    usr = userdata.objects.all()
    found = False
    for i in usr:
        if user == i.user and pas == i.password:
            found = True
            break
    if found == True:
        return render(request, 'loggedin.html')
    else:
        return render(request, 'wrong.html')
