#Need to install requests package for python
#easy_install requests
import requests
import csv

# Set the request paratbskmeters
url = 'https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_0_tbsk_testin?EXCEL&sysparm_query=active=true&sysparm_limit=10'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = '%4ez6^HvDxYN'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
#print(response.content)
data = response.CSV()
print(data)
