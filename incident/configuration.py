
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
    "webhook": [{
      "url": "https://c8204885.ngrok.io/api/incident/",
      "pattern": "((?:INC)+[0-9]{7})|((?:inc)+[0-9]{7})",
      "event": "room_message",
      "name": "incident-debug"
      }]
  }
}
