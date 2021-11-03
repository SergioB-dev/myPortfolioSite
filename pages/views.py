from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('My name is Sergio. I am a software engineer, welcome to my page.')
