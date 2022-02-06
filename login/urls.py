from django.http import HttpResponse
from . import views
from django.urls import URLPattern, include, path

urlpatterns = [
    #path('login/', views.login),
    path('', views.login),
    #path('signup/', views.signup),
    #path('saveuser/', views.saveuser, name='saveuser'),
    #path('auth/', views.auth, name='auth'),
]