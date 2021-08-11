import json
import requests
import pandas as pd
from datetime import datetime

from requests.auth import HTTPBasicAuth


host = 'https://modeanalytics.com'
org = 'solutionssandbox'
un = '3065fbd67935'
pw = '68c2d7f789437fa3acfbbbcb'

headers = {
	'Content-Type': 'application/json',
	'Accept': 'application/hal+json'
}

url = F"https://app.mode.com/api/{org}/groups"

r = requests.get(url, 
	headers=headers, 
	auth=HTTPBasicAuth(un, pw)
)

js = r.json()
groups_full = js['_embedded']['groups']
groups = [{'group_id':g['token'], 'group_type':g['group_type'], 'name':g['name']} for g in groups_full]

csv_file_name = F"{org} Workspace Group Request -" + str(datetime.now())

df = pd.DataFrame(groups)
df.to_csv(csv_file_name+".csv",index=False)

result = r.json()
if r.status_code == 200:
	print(F"A CSV file named {csv_file_name} of all user groups in {org} has been created!")
else:
	print('ERROR: Unable to complete request')
	print(r.text)
