from service_link_request_handler import messageToIncidentNumbers, getIncidentJSONWithLinks
from django.shortcuts import render
import json

# Beginnings of a json response to a HipChat webhook.
# We will fill in the "message" variable below in handleHipchatMessage()
hipChatReturnMessage = {
    "color": "green",
    "message": "",
    "notify": False,
    "message_format": "html"
}

# HipChat add-on API expects a JSON response when installing that consists
# of basic info about the webapp and a url to send POSTs to when the listener
# is triggered by a match to the supplied pattern.
config = {
    "name": "SListener",
    "description": "An add-on that listens for ServiceLink incidents \
    and returns a structured and useful response to HipChat.",
    "key": "com.gerardvh.sl-listener",
    "links": {
        "homepage": "https://gerardvh.com",
        "self": "https://sl-listener.herokuapp.com/configuration"
    },
    "capabilities": {
    "hipchatApiConsumer": {
        "scopes": [
            "send_notification"
        ]
    },
    "webhook": [{
        "url": "https://sl-listener.herokuapp.com/api/incident/",
        "pattern": "[INCinc]+[0-9]{7}",
        "event": "room_message",
        "name": "incident-debug"
        }]
    }
}

def handleHipchatMessage(message, request):
    name = message['item']['message']['from']['name'] # full name of user
    nums = messageToIncidentNumbers(message['item']['message']['message'])
    # Reduce the message text to just incident numbers (INC#######)
    slResponseObj = getIncidentJSONWithLinks(nums)
    httpResponse = render(request, 
        'hipchat.html', # HTML template to use
        {'name': name, # Pass in some variables to be used in our template
        'incidents': slResponseObj}) 
    hipChatReturnMessage['message'] = httpResponse.content 
    # Just get the formatted HTML string for our HipChat message 
    return hipChatReturnMessage
