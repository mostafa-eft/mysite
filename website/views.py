from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse('<h1>home page<h1>')

def about(request):
    return HttpResponse('<h1>about page<h1>')

def contact(request):
    return HttpResponse('<h1>contact page<h1>')
