from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def elevatorpitch(request):
    return render(request, 'elevatorpitch.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')