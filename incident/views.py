from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello, World!')


def incident(request):
    if request.method == 'GET':
        params = request.GET   
    elif request.method == 'POST':
        params = request.POST     

    return JsonResponse(params)