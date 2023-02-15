# ******************************************************************************
# ServiceNow table importer                                                    *
# Version RPC                                                                  *
# ******************************************************************************
#   02.07.2022  WZHMOEA     Initial version                                    *
#   03.07.2022  WZHMOEA     Changed to Production                              *
#   04.07.2022  WZHMOEA     Made the API call to get a servers Table from      *
#                           inctanses as in json                               *
#   05.07.2022  WZHMOEA     Trensfered the Data from json to csv with correct  *
#                           seperater                                          *
#   06.07.2022  WZHMOEA     Created other csv file containing selected country *
#   07.07.2022  WZHMOEA     Removed Name Suffix                                *
#   08.07.2022  WZHMOEA     Removed Name Suffix                                *
#   09.07.2022  WZHMOEA     Removed Name Suffix                                *
#   10.07.2022  WZHMOEA     Added a configration fila .ini to filter countries *
# ******************************************************************************

#Need to install requests package for python (requests, pandas)
#easy_install requests
# import modules:
import requests
import csv
import pandas as pd
from configparser import ConfigParser


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

# Decode the JSON response into a dictionary and use the data to create arry to be put in the created CSV
data = response.json()
ourresult = []
csvheader = ['Name (FQDN)', 'Model', 'Is virtual', 'Operating system', 'OS version', 'Comments', 'Class', 'CPU count',
             'CPU core count', 'IP address', 'RAM (MB)', 'Company identifier', 'Status', 'Serial number', 'Used for', 'location', 'model']

for x in data ['result']:
    listing = [x['name_fqdn'],x['model'],x['is_virtual'],x['operating_system'],x['os_version'],x['comments'],x['class'],x['cpu_count'],
               x['cpu_core_count'],x['ip_address'],x['ram_mb'],x['company_identifier'],x['status'],x['serial_number'],x['used_for'],x['location'],x['model']]
    ourresult.append(listing)
#Creating a CSV file contining the Servers Table including headers

with open('A4_all_config_HU.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(csvheader)
    writer.writerows(ourresult)
    reader = csv.DictReader(f)

# reading csv file
nwus_a = pd.read_csv("A4_all_config_HU.csv", sep=';')
#print("DataFrame...",nwus_a)

# select rows containing text "RBHU"
file = 'A4_config.ini'
config = ConfigParser()
config.read(file)
#from configuration file config.ini slect country name.
nwus_a = nwus_a[nwus_a['Company identifier'].str.contains(config['country'] ['Name'])]
print(nwus_a)

nwus_a.to_csv('A4_KO_config_HU.csv', encoding='utf-8', index=False, sep=';')
#df.to_csv("czhz_small_test2_50HU.csv")


print(f)
print ('done')
#print(ourresult)

#file = 'A4_config.ini'
#config = ConfigParser()
#config.read(file)
#config['country'] ['Name']