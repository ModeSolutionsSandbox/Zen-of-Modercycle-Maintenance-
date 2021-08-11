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
url = 'https://app.mode.com/api/%s/groups' % org

r = requests.get(url, 
  headers=headers, 
  auth=HTTPBasicAuth(api_token, api_password)
)
def add_user_to_group(group_id, group_name, user_id, email):
  url = '%s/api/%s/groups/%s/memberships' % (host, org, group_id)
  payload = {'membership':{'member_token': user_id}}
  
  print(url)
  print(payload)
  r = requests.post(url, auth=HTTPBasicAuth(api_token, api_password), headers=headers, json=payload)
  
  if r.status_code == 200:
    print('%s successfully added!' % email)
  else:
    print('ERROR: Failed to add %s.' % email)
    print(r.json())
    
# Update with the actual relative file path of the CSV with the list of members. CVS File should have the follwing columns: name, email, invite_message		
df = pd.read_csv("ENTER FILE PATH")
df.apply(lambda x: add_user_to_group(x['group_id'],x['group_name'],x['user_id'],x['email']), axis=1)

  
