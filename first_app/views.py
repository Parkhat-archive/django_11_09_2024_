from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_view(request):
    return HttpResponse("<h1>Hello! It's my first view!</h1>")
