import json
import re

from service_link_request_handler import getIncidentInfo

pattern1 = re.compile("((?:INC)+[0-9]{7})")
pattern2 = re.compile("((?:inc)+[0-9]{7})")

incidentBaseUrl = "https://umichprod.service-now.com/nav_to.do?uri=incident.do?sys_id="

testMessage = """Testing typing53 numbers and Incidents 
in this format INC0434690//\ or , +_+ 
INC0573812, inc1230088nasl plus iNc2314421 or INC23145"""

def messageToIncidentNumbers(message):
    # Accepts a string, returns incident numbers matching a regex
    incidentList = []
    print "made it to messageToIncidentNumbers"
    for incident in pattern1.findall(message):
        incidentList.append(incident)

    for incident in pattern2.findall(message):
        incidentList.append(incident)

    return incidentList


def incidentNumbersToLinks(incidentList):
    # Accepts list of incident numbers and returns valid links
    jsonObj = getIncidentInfo(incidentList)
    print incidentList
    sys_idList = []
    linkList = []
    for obj in jsonObj:
        sys_idList.append(obj['sys_id'])
        obj['incidentLink'] = incidentBaseUrl + obj['sys_id']

    for sys_id in sys_idList:
        incidentLink = incidentBaseUrl + sys_id
        linkList.append(incidentLink)

    return linkList, jsonObj


# incidentNumbersToLinks(messageToIncidentNumbers(testMessage))
