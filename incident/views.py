from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
from incident_parser import messageToIncidentNumbers, incidentNumbersToLinks
from configuration import config
from hipchatHandler import handleHipchatMessage

# Create your views here.
def configuration(request):
    return JsonResponse(config,safe=False)

def index(request):
    return HttpResponse('Hello, World!')

def incidentAPI(request):
    if request.method == 'POST':
        jsonPOST = json.loads(request.body)
        # print json.dumps(jsonPOST)
        print "about to send to handleHipchatMessage()"
        hipChatReturnMessage = handleHipchatMessage(jsonPOST, request)
        return JsonResponse(hipChatReturnMessage)
    