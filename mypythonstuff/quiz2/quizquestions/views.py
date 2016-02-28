from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    login(request,username)
    return HttpResponse("Hello, world. You're at the login session for user="+username)



