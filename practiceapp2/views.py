from django.shortcuts import render

# Create your views here. #added 24-04-26
def home(request):
    return render(request, 'practiceapp2/index.html') 
