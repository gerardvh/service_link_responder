from incident_parser import messageToIncidentNumbers, incidentNumbersToLinks
from django.shortcuts import render
import json
import markdown

hipChatReturnMessage = {
    "color": "green",
    "message": "",
    "notify": False,
    "message_format": "html"
}

def handleHipchatMessage(message, request):
    print "made it to handleHipchatMessage()"
    # print json.dumps(message)
    name = message['item']['message']['from']['name']
    nums = messageToIncidentNumbers(message['item']['message']['message'])
    links, slResponseObj = incidentNumbersToLinks(nums)
    print "about to try and render"
    httpResponse = render(request, 'hipchat.html', {'name': name, 'incidents': slResponseObj})
    print "successfully rendered"
    hipChatReturnMessage['message'] = httpResponse.content
    print "successfully added to message"
    return hipChatReturnMessage
