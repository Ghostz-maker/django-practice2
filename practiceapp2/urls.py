# added 24-04-26
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]