# ******************************************************************************
# Using ServiceNow REST API, Table API, GET method                             *
# ServiceNow table Export                                                      *
# Version RPC                                                                  *
# ******************************************************************************
#   04.07.2022  WZHMOEA     Initial version                                    *
#   03.07.2022  WZHMOEA     Changed to Production                              *
#   04.07.2022  WZHMOEA     Made the API call to get a servers Table from      *
#                           inctanses as in json                               *
#   05.07.2022  WZHMOEA     Trensfered the Data from json to csv with correct  *
#                           seperater                                          *
#   06.07.2022  WZHMOEA     Filtered csv file containing selected country      *
#   10.07.2022  WZHMOEA     Added a configration fila .ini to filter countries *
# ******************************************************************************

#Need to install requests package for python (requests, CSV, pandas, configparser)
# import modules:
import requests
import csv
import pandas as pd
from configparser import ConfigParser

# -----------------------------------------------------------------------------
# ServiceNow URL and Login credentials for the instance                       -
# -----------------------------------------------------------------------------

# Set the request parameters
url = 'https://dev135762.service-now.com/api/now/table/x_932324_small_t_0_czhuko?sysparm_limit=16'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'oq0+TOa@8nHH'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# -----------------------------------------------------------------------------
#ServiceNow URL and Login credentials for the instance                       -
# -----------------------------------------------------------------------------

# Decode the JSON response into a dictionary and use the data to create arry to be put in CSV file
data = response.json()
ourresult = []
csvheader = ['Name (FQDN)', 'Model', 'Is virtual', 'Operating system', 'OS version', 'Comments', 'Class', 'CPU count',
             'CPU core count', 'IP address', 'RAM (MB)', 'Company identifier', 'Status', 'Serial number', 'Used for', 'location', 'model']

for x in data ['result']:
    listing = [x['name_fqdn'],x['model'],x['is_virtual'],x['operating_system'],x['os_version'],x['comments'],x['class'],x['cpu_count'],
               x['cpu_core_count'],x['ip_address'],x['ram_mb'],x['company_identifier'],x['status'],x['serial_number'],x['used_for'],x['location'],x['model']]
    ourresult.append(listing)

# Loading ServiceNow table data into Pandas
# Select rows containing text "RBHU"
file = 'A4_config.ini'
config = ConfigParser()
config.read(file)
filename = (config['country'] ['Name'])
# Creating a CSV file contining the Servers Table including headers
with open(filename + '.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(csvheader)
    writer.writerows(ourresult)
    reader = csv.DictReader(f)


nwus_a = pd.read_csv(filename + '.csv', sep=';')



# From configuration file config.ini slect country name.
nwus_a = nwus_a[nwus_a['Company identifier'].str.contains(config['country'] ['Name'])]
nwus_a.to_csv(filename + '.csv', encoding='utf-8', index=
False, sep=';')

# -----------------------------------------------------------------------------
# Run completed                                                               -
# -----------------------------------------------------------------------------

print ('done')
