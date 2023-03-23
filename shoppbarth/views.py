from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Home Casa Sei la")

def contato(request):
    return HttpResponse("CONTATO")

def sobre(request):
    return HttpResponse("SOBRE")