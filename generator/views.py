from django.shortcuts import render
import random
#from django.http import HttpResponse

# Create your views here.
def about(request):
  return render(request, 'generator/about.html')

def home(request):
  return render(request, 'generator/home.html')

def password(request):
  characteres = list('abcdefghijklmnopqrstuvwxyz')
  generetedPassword = ''

  length = int(request.GET.get('length'))
  if length > 14:
    length = 14

  if request.GET.get('uppercase'):
    characteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

  if request.GET.get('special'):
    characteres.extend(list('!@#$%^&*()_+/-><:;'))

  if request.GET.get('numbers'):
    characteres.extend(list('0123456789'))

  for x in range(length):
    generetedPassword += random.choice(characteres)

  return render(request, 'generator/password.html', {'password' : generetedPassword})