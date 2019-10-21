from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def home(request):
    
    return render(request,"home.html")


def nosotros(request):
    
    return render(request,"nosotros.html")

def proyectos(request):
    
    return render(request,"proyectos/proyectos.html")

def contacto(request):
    
    return render(request,"contacto.html")

def singularity(request):
    
    return render(request,"proyectos/singularity.html")

def singularity_import(request):
    
    return render(request,"proyectos/singularity-import.html")

def import_acount(request):
    
    return render(request,"import/import-account.html")

def cart(request):
    
    return render(request,"import/cart.html")

def coming_soon(request):
    
    return render(request,"import/coming-soon.html")

def checkout(request):
    
    return render(request,"import/checkout.html")

def product_detail(request):
    
    return render(request,"import/product-detail.html")

def shop(request):
    
    return render(request,"import/shop.html")