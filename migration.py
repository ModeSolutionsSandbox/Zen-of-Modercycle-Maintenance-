import pandas
import json
import requests
from requests.auth import HTTPBasicAuth

host = 'https://app.mode.com'
org = 'ADD WORKSPACE USERNAME'
# un and pw are api token and secret that can be generated under account dropdown -> Account -> API Tokens
un = 'ADD_API_TOKEN'
pw = 'ADD_API_TOKEN_SECRET'

template_report_token = 'ADD_TEMPLATE_REPORT_TOKEN'
template_run_token = 'ADD_ANY_RUN_OF_THAT_REPORT'

# SEE example of file structure in mock_migiration2.csv
df = pandas.read_csv('ADDCSVFILENAME.csv')
reports_dict = df

# Build Dictionary of queries per dashboard
migration_list = df.groupby(['space_token','Report Name'])[['query_name','datasource','query']].apply(lambda x: x.set_index('query_name').to_dict(orient='index')).to_dict()


def build_new_reports(template_report_token,report_run_token):
# Clone template report
  url = '%s/api/%s/reports/%s/runs/%s/clone' % (host, org,template_report_token,report_run_token)
  headers = {'Content-Type': 'application/json'}
  r = requests.post(url, headers=headers, auth=HTTPBasicAuth(un, pw))
  new_report_token = r.json()['token']
  status = r.status_code
  print("This was the status of cloning the report - %s and here is the report token %s" %(status,new_report_token))
  # Return new report token
  return new_report_token

# Add title to report and move to the proper collection
def update_report_details(report_token,space_token,report_name):

    url = '%s/api/%s/reports/%s/' % (host, org,report_token)

    headers = {'Content-Type': 'application/json'}
    payload = {
    "report": {

        'name':'%s'%(report_name),
        'space_token':'%s' % (space_token)

      }
     }
    r = requests.patch(url, json=payload,headers=headers, auth=HTTPBasicAuth(un, pw))
    print(r)
# Add queries to the desired report. IMPORTANT make sure that datasource ID is valid, if it isn't, this method will return a 404
def add_queries(report_token,query,query_name,datasource):
    
    url = '%s/api/%s/reports/%s/queries' % (host, org,report_token)
    headers = {'Content-Type': 'application/json'}
    payload = {
    "query": {

        'raw_query':'%s'%(query),
        'data_source_id':'%s' % (datasource),
        'name':'%s' %(query_name)

      }
     }
    r = requests.post(url, json=payload,headers=headers, auth=HTTPBasicAuth(un, pw))
    print('%s added to report with status %s' %(query,r.status_code))
# Create a report run of the newly added Query
def create_report_run(report_token):
  url = '%s/api/%s/reports/%s/runs' % (host, org,report_token)
  headers = {'Content-Type': 'application/json'}
  r = requests.post(url, headers=headers, auth=HTTPBasicAuth(un, pw))



# Iterate through reports
for key, value in migration_list.items():
    space_token = key[0]
    report_name = key[1]
    report_queries = value
    # Clone template report and return new report token 
    new_report_token = build_new_reports(template_report_token,template_run_token)
    # Update report name and space
    update_report_details(new_report_token,space_token,report_name)

    # Iterate through the queries in a report 
    for key,value in report_queries.items():
        datasource = value['datasource']
        query_statement = value['query']
        query_name = key
        print(new_report_token)
        add_queries(new_report_token,query_statement,query_name,1)
        create_report_run(new_report_token)
    
