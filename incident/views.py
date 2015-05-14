from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import json

config = {
  "name": "Service_Link_Responder",
  "description": "An add-on that does wonderful things",
  "key": "com.example.myaddon",
  "links": {
    "homepage": "https://example.com/myaddon",
    "self": "https://example.com/myaddon/capabilities"
  },
  "capabilities": {
    "hipchatApiConsumer": {
      "scopes": [
        "send_notification"
      ]
    },
    "webhook": [
      {"url": "https://c8204885.ngrok.io/api/incident",
      "pattern": "((?:INC)+[0-9]{7})|((?:inc)+[0-9]{7})",
      "event": "room_message",
      "name": "incident-debug"
      }
    ]

  }
}

# Create your views here.
def configuration(request):
    return JsonResponse(config,safe=False)

def index(request):
    return HttpResponse('Hello, World!')


def incident(request):
    if request.method == 'GET':
        params = request.GET   
    elif request.method == 'POST':
        params = request.POST     

    return JsonResponse(params)