# Requires Python 3 and the following libraries 
import requests
import pandas as pd

from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
org  = 'ENTER WORKSPACE NAME FOUND IN URL'
# You will need to generate an API Token & Password - Instructions on Mode Help Site. - https://mode.com/help/articles/api-reference/#generating-api-tokens
api_token    = 'NEW API TOKEN'
api_password = 'NEW API PASSWORD'

headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/hal+json'
}
url = '%s/api/%s/invites' % (host, org)

def send_invite(email, message):
	values = """
		{
			"invite": {
				"invitee": { "email": "%s" },
				"message": "%s"
			}
		}
	""" % (email, message)
	
	r = requests.post(url, 
		data=values, 
		headers=headers, 
		auth=HTTPBasicAuth(api_token, api_password)
	)
	
	if r.status_code == 200:
		print('%s successfully invited!' % email)
	else:
		print('ERROR: invite to %s failed.' % email)
		print(r.text)
# Update with the actual releative file path of the CSV with the list of members. CVS File should have the follwing columns: name, email, invite_message		
df = pd.read_csv("ENTER FILE PATH")
df.apply(lambda x: send_invite(x['email'],x['invite_message']), axis=1)
