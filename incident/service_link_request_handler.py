import requests
import json
import os
import re

ciUrl = 'https://umichprod.service-now.com/api/now/table/cmdb_ci'
incUrl = 'https://umichprod.service-now.com/api/now/table/incident'
user = os.environ.get('SL_USER') # User saved in .env
pwd = os.environ.get('SL_PASSWORD') # Pass saved in .env

incidentPattern = re.compile("((?:INC)+[0-9]{7})", re.IGNORECASE) 
incidentLinkBaseUrl = "https://umichprod.service-now.com/nav_to.do?uri=incident.do?sys_id="

limit = 10 # Used in process() to limit the number of items returned from ServiceLink
displayName = True # Adjusts response from SL to show full names instead of id's for user and locations

def process(query, url):
    parameters = {}
    parameters['sysparm_limit'] = limit
    parameters['sysparm_display_value'] = displayName
    parameters['sysparm_query'] = query  # Take an encoded query string for SL 
    response = requests.get(url, # make request at our passed-in url 
        auth=(user, pwd), # Use auth info from .env
        headers={"Accept": "application/json"}, # Return json from SL
        params=parameters) # Pass in our param dict to tailor response
    if response.status_code == 200: # if we get a good response
        return response.json() # Send back the full json


def getIncidentInfo(incidents):
    """Sends a list of incident numbers as a query to ServiceLink
    and returns a json response including all items at the top level."""
    query = getIncidentQueryString(incidents)
    jsonObj = process(query, incUrl)
    return jsonObj['result']


def getIncidentQueryString(queryList):
    """Takes a list of incident numbers and returns a proper query string
    for the ServiceLink API."""
    if len(queryList) == 1: # No need for ^OR with one query
        return "number=" + queryList[0]
    else: # Add ^OR for each subsequent query to get multiples back
        queryString = "number=" + queryList[0]
        for query in queryList[1:]:
            queryString += "^ORnumber=" + query
        return queryString


def messageToIncidentNumbers(message):
    # Currently assuming we are working with incidents
    # Could make different patterns for different things
    return incidentPattern.findall(message)


def getIncidentJSONWithLinks(incidentList):
    jsonObj = getIncidentInfo(incidentList)
    for obj in jsonObj:
        obj['incident_link'] = incidentLinkBaseUrl + obj['sys_id']
    return jsonObj