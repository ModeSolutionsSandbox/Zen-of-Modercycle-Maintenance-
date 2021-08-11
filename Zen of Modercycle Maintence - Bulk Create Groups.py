# Requires Python 3 and the following libraries 
import json
import requests
import pandas as pd

from requests.auth import HTTPBasicAuth


host = 'https://modeanalytics.com'
# This is found in the subdomain of the URL of your Mode Workspace URL 
org = 'YOUR WORKSPACE NAME'
# You will need to generate an API Token & Password - Instructions on Mode Help Site. - https://mode.com/help/articles/api-reference/#generating-api-tokens
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
# Update with the actual relative file path of the CSV with the list of members. CVS File should have the follwing columns: name, email, invite_message
df = pd.read_csv("ENTER FILE PATH")
df.apply(lambda x: create_group(x['group_name'],), axis=1)
