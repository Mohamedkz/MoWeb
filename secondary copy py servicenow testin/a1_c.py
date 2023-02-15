#Need to install requests package for python
#easy_install requests
import requests
import csv
import pandas as pd


# Set the request parameters
#url = 'https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_0_tbsk_testin?sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_limit=10'
#url = 'https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_1_czhu_small?sysparm_limit=1'
#https://dev135762.service-now.com/api/now/table/x_932324_tbsk_te_1_czhu_small?sysparm_limit=1
#url = 'https://dev135762.service-now.com/api/now/table/x_932324_small_t_0_czhu_small?sysparm_limit=31'
url = 'https://dev135762.service-now.com/api/now/table/x_932324_small_t_0_czhuko?sysparm_limit=10'



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
with open('czhz_small_test2_500.csv','w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourresult)
    reader = csv.DictReader(f)

# reading csv file
nwus_a = pd.read_csv("czhz_small_test2_500.csv")
#print("DataFrame...",nwus_a)

# select rows containing text "country"
nwus_a = nwus_a[nwus_a['Company identifier'].str.contains('RBHU')]
print(nwus_a)

nwus_a.to_csv('czhz_small_test2_50HU.csv', encoding='utf-8')
#df.to_csv("czhz_small_test2_50HU.csv")


#print("Fetching rows with text Lamborghini ...",nwus_a)


   # with open('nwu_servers_line402.csv', 'w') as new_files:
        #fieldnames = ['Name (FQDN)', 'Model', 'Is virtual', 'Operating system', 'OS version', 'Comments', 'Class', 'CPU count',
             #'CPU core count', 'IP address', 'RAM (MB)', 'Company identifier', 'Status', 'Serial number', 'Used for', 'location', 'model']
       # writer = csv.DictWriter(new_files, fieldnames=fieldnames, delimiter=',')
       # writer.writeheader()
        #for line in ourresult:
            #if line[int['Company identifier']] == [int["RBHU"]]:
               #writer.writerow([line['Company identifier'] == ["RBHU"]])
            #print (line[5])
            #else:
                 #print('not found')
#print ('done')
#print(ourresult)
