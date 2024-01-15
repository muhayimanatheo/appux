from django.shortcuts import render
from django.http import HttpResponse

def design(request):
    return HttpResponse('Hello Theo')