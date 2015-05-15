import json
import re

pattern1 = re.compile("((?:INC)+[0-9]{7})")
pattern2 = re.compile("((?:inc)+[0-9]{7})")

testMessage = """Testing typing53 numbers and Incidents 
in this format INC0434690//\ or , +_+ 
INC0573812, inc1230088nasl plus iNc2314421 or INC23145"""

def messageToIncidentNumbers(message):
    # Accepts a string, returns incident numbers matching a regex
    incidentList = []
    for incident in pattern1.findall(message):
        incidentList.append(incident)

    for incident in pattern2.findall(message):
        incidentList.append(incident)

    return incidentList


def incidentNumbersToLinks(incidentList):
    # Accepts list of incident numbers and returns valid links
    for incident in incidentList:
        print ""