from django.shortcuts import render
from django.http import HttpResponse


def supports(request):
    return HttpResponse('liste de tout les support') 


