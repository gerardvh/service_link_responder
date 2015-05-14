from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse


# Create your views here.
def configuration(request):
    return JsonResponse({
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
      "https://guarded-spire-1898.herokuapp.com/api/incident",
      "((?:INC)+\d{7})|((?:inc)+\d{7})",
      "room_message",
      "incident-debug"
      ]

  }
})

def index(request):
    return HttpResponse('Hello, World!')


def incident(request):
    if request.method == 'GET':
        params = request.GET   
    elif request.method == 'POST':
        params = request.POST     

    return JsonResponse(params)