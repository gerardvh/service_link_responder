from incident_parser import messageToIncidentNumbers, incidentNumbersToLinks
from django.shortcuts import render
import json

hipChatReturnMessage = {
    "color": "green",
    "message": "",
    "notify": False,
    "message_format": "html"
}

def handleHipchatMessage(message, request):
    print "made it to handleHipchatMessage()"
    # print json.dumps(message)
    nums = messageToIncidentNumbers(message['item']['message']['message'])
    
    links = incidentNumbersToLinks(nums)
    print "about to try and render"
    httpResponse = render(request, 'hipchat.html', {'links': links })
    print "successfully rendered"
    hipChatReturnMessage['message'] = httpResponse.content

    return hipChatReturnMessage