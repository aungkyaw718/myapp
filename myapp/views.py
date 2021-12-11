from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request,"customer/index.html")

def customer(request):
    return render (request,"customer/customer.html")

