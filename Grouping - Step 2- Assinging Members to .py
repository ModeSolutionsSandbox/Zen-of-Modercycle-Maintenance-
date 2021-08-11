import requests
import pandas as pd

from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
org  = 'demo'

api_token    = '3065fbd67935'
api_password = '68c2d7f789437fa3acfbbbcb'


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
    
df = pd.read_csv("/Users/terrybrooks/Desktop/Buckets.csv")
df.apply(lambda x: add_user_to_group(x['group_id'],x['group_name'],x['user_id'],x['email']), axis=1)

  