import json
import requests
import pandas as pd

from requests.auth import HTTPBasicAuth


host = 'https://modeanalytics.com'
# This is found in the subdomain of the URL of your Mode Workspace URL 
org = 'YOUR WORKSPACE NAME'
# You will need to generate an API Token & Password
un = 'API TOKEN'
pw = 'API PASSWORD'

def create_group(group_name):
	url = '%s/api/%s/groups' %(host, org)
	headers = {'Content-Type': 'application/json'}
	payload = {'embed[new_group_membership]':'1', 'user_group':{'name': group_name}}
	r = requests.post(url, auth=HTTPBasicAuth(un, pw), headers=headers, json=payload)
	result = r.json()
	if r.status_code == 200:
		print('%s user group successfully created!' % group_name)
	else:
		print('ERROR: invite to %s failed.' % group_name)
		print(r.text)
	
	
	return result

df = pd.read_csv("/Users/terrybrooks/Desktop/API_Bulk_Create.csv")
df.apply(lambda x: create_group(x['group_name'],), axis=1)
