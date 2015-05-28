from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json
from hipchatHandler import handleHipchatMessage, config

# Create your views here.
def configuration(request):
    # Returns the config json string to HipChat when installing the
    # add-on to a room.
    return JsonResponse(config,safe=False)

def index(request):
    # Currently just an API, no need for interface, may want to add
    # something in the future here for configuration within HipChat.
    # Returns a blank page.
    return HttpResponse('')

def incidentAPI(request):
    # The HipChat API will send a POST message to our specified URL
    # containing a json formatted body. The specifics of that json body
    # are dealt with in the handleHipChatMessage() function.
    if request.method == 'POST':
        jsonPOST = json.loads(request.body)
        hipChatReturnMessage = handleHipchatMessage(jsonPOST, request)
        return JsonResponse(hipChatReturnMessage)

    else:
        return HttpResponse('')
    