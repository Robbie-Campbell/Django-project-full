from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hi")

def detail(request, name_id):
    return HttpResponse("You are looking at %s. order" % name_id)