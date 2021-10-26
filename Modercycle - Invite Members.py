"""
Send Email Invitations to the Mode Workspace Identified in the org variable

Inputs:
org - Mode Workspace username found in the subdomain of the Workspace URL
host - This is a durable global variable - Do Not Modify 
api_token - API token used for the authentication - Instructions for how to generate an API Token & Password on Mode Help Site. - https://mode.com/help/articles/api-reference/#generating-api-tokens 
api_password - API passeword used for authentication - Instructions for how to generate an API Token & Password on Mode Help Site. - https://mode.com/help/articles/api-reference/#generating-api-tokens 

Returns: 
  - If Successful - Confirmation Message with the email
  - If Failed - Failed Notice with Status Code 
"""
import requests
import pandas as pd

from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
org  = 'ENTER WORKSPACE NAME FOUND IN URL'

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
# Update with the actual relative file path of the CSV with the list of members. CVS File should have the following columns: name, email, invite_message		
df = pd.read_csv("ENTER FILE PATH")
df.apply(lambda x: send_invite(x['email'],x['invite_message']), axis=1)
