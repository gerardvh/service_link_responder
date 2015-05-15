import requests
import json

ciUrl = 'https://umichprod.service-now.com/api/now/table/cmdb_ci'
incUrl = 'https://umichprod.service-now.com/api/now/table/incident'
user = '***REMOVED***'
pwd = '***REMOVED***'

# url can have multiple requirements put on it, separated by '&,' example:
parameters = {}
limit = 10
fieldsToReturn = 'location,serial_number,name'
displayName = True

headers = {"Accept": "application/json"}

def process(query):
    # addParameters(p)
    parameters = {}
    parameters['sysparm_limit'] = limit
    # parameters['sysparm_fields'] = fieldsToReturn
    parameters['sysparm_display_value'] = displayName
    # query = raw_input('enter your query parameters: ')
    parameters['sysparm_query'] = query   
    response = requests.get(incUrl, auth=(user, pwd), headers=headers, params=parameters)
    # print json.dumps(response.json(), indent=2)
    if response.status_code == 200:
        return response.json()


def getIncidentInfo(incidents):
    query = getQueryString(incidents)


def getQueryString(queryList):
    if queryList.length == 1:
        return "" + queryList[0]
    else:
        queryString = "" + queryList[0]
        for query in queryList[1:]:
            queryString += "^OR" + query

        return queryString
