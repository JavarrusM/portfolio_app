from django.shortcuts import render
from django.http import HttpResponse
import random

# app = 'project'

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''

    length = int(request.GET.get('length'))

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    characters = list(lowercase)

    if request.GET.get('uppercase'):
        uppercase = list(lowercase.upper())
        characters.extend(uppercase)

    if request.GET.get('numbers'):
        numbers = list('0123456789')
        characters.extend(numbers)
    
    if request.GET.get('special'):
        special = list('!@#$%^&*()-+<>?/\|~')
        characters.extend(special)

    for _ in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})