from django.shortcuts import render

from django.http import HttpResponse


def parent(request):
    return HttpResponse("Здесь будет ЭЖ для родителя")
