import requests
import json

url = 'https://umichprod.service-now.com/api/now/table/cmdb_ci'
user = '***REMOVED***'
pwd = '***REMOVED***'

# url can have multiple requirements put on it, separated by '&,' example:
parameters = {}
limit = 10
fieldsToReturn = 'location,serial_number,name'
displayName = True

headers = {"Accept":"application/json"}