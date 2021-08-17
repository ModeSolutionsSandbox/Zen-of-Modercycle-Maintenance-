import requests
import pandas as pd

from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
org  = 'MODE WORKSPACE NAME'
# You will need to generate an API Token & Password
api_token    = 'API TOKEN'
api_password = 'API PASSWORD'

headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/hal+json'
}
def create_group(group_name):
	url = '%s/api/%s/groups' %(host, org)
	payload = {'embed[new_group_membership]':'1', 'user_group':{'name': group_name}}
	r = requests.post(url, auth=HTTPBasicAuth(api_token, api_password), headers=headers, json=payload)
	result = r.json()
	if r.status_code == 200:
		print('%s user group successfully created!' % group_name)
	else:
		print('ERROR: unable to create to %s group' % group_name)
		print(r.text)
		
		
	return result
df = pd.read_csv('UPDATE_FILE_PATH')
df.apply(lambda x: create_group(x['group_name'],), axis=1)