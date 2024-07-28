from django.shortcuts import render

from django.http import HttpResponse

def teacher(request):
    return HttpResponse("Здесь будет версия ЭЖ для учителей")

