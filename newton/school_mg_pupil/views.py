from django.shortcuts import render
from django.http import HttpResponse

def pupil_profile(request):
    return HttpResponse("Здесь будет версия ЭЖ для ученика")
# Create your views here.
