from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
from hipchatHandler import handleHipchatMessage, config

# Create your views here.
def configuration(request):
    return JsonResponse(config,safe=False)

def index(request):
    return HttpResponse('Hello, World!')

def incidentAPI(request):
    if request.method == 'POST':
        jsonPOST = json.loads(request.body)
        hipChatReturnMessage = handleHipchatMessage(jsonPOST, request)
        return JsonResponse(hipChatReturnMessage)
    