from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
from incident_parser import messageToIncidentNumbers, incidentNumbersToLinks
from configuration import config

# Create your views here.
def configuration(request):
    return JsonResponse(config,safe=False)

def index(request):
    return HttpResponse('Hello, World!')

def incidentAPI(request):
    hipChatMessage = {}
    if request.method == 'POST':
        jsonPOST = json.loads(request.body)
        nums = messageToIncidentNumbers(jsonPOST['item']['message']['message'])
        links = incidentNumbersToLinks(nums)
        returnMessage = ""
        # print jsonPOST['item']['message']['message']
        for link in links:
            returnMessage += " And another one: " + link
        hipChatMessage = {
            "color": "green",
            "message": returnMessage,
            "notify": True,
            "message_format": "text"
        }

    
    return JsonResponse(hipChatMessage)
    