from django.shortcuts import render

# Create your views here. #added 24-04-26
def home(request):
    return render(request, 'practiceapp2/index.html') 

#updated 27-04-26
def about(request):
    return render(request, 'practiceapp2/about.html')

def contact(request):
    return render(request, 'practiceapp2/contact.html')

from .models import Game

def home(request):
    games = Game.objects.all()
    return render(request, 'practiceapp2/index.html', {'games': games})