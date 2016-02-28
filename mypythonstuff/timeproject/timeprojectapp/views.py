from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    val=request.session['hero']
    if (val  == None):
        request.session['hero']='Heeralal'
    else:
        request.session['hero']=val+'Heeralal'
    return HttpResponse("Hello, world. You're at the hitmeddd index.")


