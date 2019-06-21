from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')



