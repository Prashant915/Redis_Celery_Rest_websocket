from django.shortcuts import render
from .tempcelery import add
# Create your views here.

def index(request):
    add.delay(2,3)
    print(add)
    pass