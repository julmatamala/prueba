from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.conf import settings
import os

# Create your views here.
def petscop_view(request):
    context = {
    }
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def carusel(request):
    return render(request, 'carusel.html')

def about_us(request):
    return render(request, 'aboutus.html')

def register(request):
    return render(request, 'register.html')

def carrito(request):
    return render(request, 'carrito.html')