import requests
import json
import os

ciUrl = 'https://umichprod.service-now.com/api/now/table/cmdb_ci'
incUrl = 'https://umichprod.service-now.com/api/now/table/incident'
user = os.environ.get('SL_USER')
pwd = os.environ.get('SL_PASSWORD')


parameters = {}
limit = 10
fieldsToReturn = 'location,serial_number,name'
displayName = True

headers = {"Accept": "application/json"}

def process(query, url):
    print "made it to process()"
    parameters = {}
    parameters['sysparm_limit'] = limit
    # parameters['sysparm_fields'] = fieldsToReturn
    parameters['sysparm_display_value'] = displayName
    parameters['sysparm_query'] = query   
    
    response = requests.get(url, auth=(user, pwd), headers=headers, params=parameters)
    # print json.dumps(response.json(), indent=2)
    if response.status_code == 200:
        return response.json()


def getIncidentInfo(incidents):
    query = getQueryString(incidents)
    print query
    jsonObj = process(query, incUrl)
    return jsonObj['result']


def getQueryString(queryList):
    if len(queryList) == 1:
        return "number=" + queryList[0]
    else:
        queryString = "number=" + queryList[0]
        for query in queryList[1:]:
            queryString += "^ORnumber=" + query
        return queryString
