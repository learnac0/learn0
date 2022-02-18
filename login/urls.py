from django.http import HttpResponse
from . import views
from django.urls import URLPattern, include, path

urlpatterns = [
    #path('login/', views.login),
    #path('dino/', views.dino),
    path('', views.game),
    #path('1/', views.gravity),
    #path('mario/', views.mario),
    #path('coil/', views.coil),
    #path('2048/', views.tzfe),
    #path('signup/', views.signup),
    #path('saveuser/', views.saveuser, name='saveuser'),
    path('auth/', views.auth, name='auth'),
]