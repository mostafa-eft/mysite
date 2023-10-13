from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
