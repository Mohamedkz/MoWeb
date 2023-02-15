#Need to install requests package for python
#easy_install requests
import requests
import csv


# Set the request parameters
#url = 'https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_0_tbsk_testin?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_limit=10'
#url = 'https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_1_czhu_small?sysparm_limit=1'
#https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_1_czhu_small?sysparm_limit=1
url = 'https://dev135762.service-now.com/api/now/table/x_932324_small_t_0_czhu_small?sysparm_limit=1'


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

# Decode the JSON response into a dictionary and use the data to create arry whcih is in CSV
data = response.json()
ourresult = []
csvheader = ['Name (FQDN)', 'Model', 'Is virtual', 'Operating system', 'OS version', 'Comments', 'Class', 'CPU count',
             'CPU core count', 'IP address', 'RAM (MB)', 'Company identifier', 'Status', 'Serial number', 'Used for', 'location', 'model'] #'used_for', 'Location', 'cpu_core_count', 'sys_created_by', 'status']
#csvheader = ['Name (FQDN)', 'comments', 'ram_mb', 'os_version', 'sys_mod_count', 'serial_number', 'company_identifier', 'ip_address', 'sys_updated_on', 'name_fqdn', 'sys_tags', 'cpu_count', 'sys_id', 'sys_updated_by', 'sys_created_on', 'operating_system', 'location', 'model', 'used_for', 'class', 'cpu_core_count', 'sys_created_by', 'status']

for x in data ['result']:
    #listing = [x['is_virtual'],x['comments'],x['ram_mb'],x['os_version'],x['sys_mod_count'],x['serial_number'],x['company_identifier'],x['ip_address'],x['sys_updated_on'],x['name_fqdn'],x['sys_tags'],x['cpu_count'],x['sys_id'],x['sys_updated_by'],x['sys_created_on'],x['operating_system'],x['location'],x['model'],x['used_for'],x['class'],x['cpu_core_count'],x['sys_created_by'],x['status']]
    listing = [x['name_fqdn'],x['model'],x['is_virtual'],x['operating_system'],x['os_version'],x['comments'],x['class'],x['cpu_count'],
               x['cpu_core_count'],x['ip_address'],x['ram_mb'],x['company_identifier'],x['status'],x['serial_number'],x['used_for'],x['location'],x['model']] #,x['sys_mod_count'],x['sys_updated_on'],x['sys_tags'],x['sys_id'],x['sys_updated_by'],x['sys_created_on'],x['sys_created_by']]
    ourresult.append(listing)
with open('czhz_small_test1.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourresult)
print ('done')
#print(ourresult)
