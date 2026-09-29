from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#django is an folder where http handles all about http related things it is a folder. HttpResponse is a file


def home(request):
    return HttpResponse("Welcome to Tushar Website")

def about(request):
    return HttpResponse("I am learning Django Backend")

def contact(request):
    return HttpResponse("Contact Page")

#ORM Mental Model
# Python Object ----> Django ORM -----> DataBase Row



