# added 24-04-26
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home),
    #updated on 27-04-26
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]