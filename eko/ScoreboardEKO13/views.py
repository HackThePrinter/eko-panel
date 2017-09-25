# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Hackan")

# Create your views here.
