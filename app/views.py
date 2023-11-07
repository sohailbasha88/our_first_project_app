from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('hi jam pandu how are you'),

def jigelrani(request):
    return HttpResponse('i am not there'),
