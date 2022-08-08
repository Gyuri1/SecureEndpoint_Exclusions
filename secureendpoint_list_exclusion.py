#!/usr/bin/env python3

'''
This script will list exclusions of a Secure Endpoint Org.
This script works in US / NAM Secure Endpoint Cloud.

More information:
https://developer.cisco.com/docs/secure-endpoint/#!authentication
https://developer.cisco.com/docs/secure-endpoint/#!exclusions

'''

import requests
import json
import sys

#SecureX Client
#Please update these values according to this doc:
#https://developer.cisco.com/docs/secure-endpoint/#!authentication
Client_ID ="client-333"
Client_Pass ="wwww"

url_token= "https://visibility.amp.cisco.com/iroh/oauth2/token"

headers = { 'Content-Type': 'application/x-www-form-urlencoded', \
            'Accept': 'application/json'}

resp = requests.post(url_token, headers=headers, data='grant_type=client_credentials', auth=(Client_ID, Client_Pass))

#print(resp.status_code)
if resp.status_code != 200:
    print("Failed to add exclusion because IDP login was unsuccessful, terminating!")
    sys.exit()
else:
    json_resp = json.loads(resp.text)
    token= json_resp["access_token"]
    print("SecureX Token was received")

    amp_access_token_url="https://api.amp.cisco.com/v3/access_tokens"
    headers = { 'Authorization': 'Bearer '+token }
        
    resp2 = requests.post(amp_access_token_url, headers=headers)
    #print(resp2.text)

    json_resp = json.loads(resp2.text)
    token2= json_resp["access_token"]
    print("Secure Endpoint Token was received")

    headers = { 'Authorization': 'Bearer '+token2}
    amp_org_url='https://api.amp.cisco.com/v3/organizations?size=10'  
    resp3 = requests.get(amp_org_url, headers=headers)
    #print(resp3.text)

    json_resp = json.loads(resp3.text)
    orgs_number= json_resp["meta"]["total"] 
    print("Number of Orgs:", orgs_number)

    org_name= json_resp["data"][0]["name"]
    org_id= json_resp["data"][0]["organizationIdentifier"]
    print("Name of the 1st Org:", org_name)

   
    amp_exc_sets_url='https://api.amp.cisco.com/v3/organizations/'+org_id+'/exclusion_sets?size=10'  
    resp4 = requests.get(amp_exc_sets_url, headers=headers)
    #print(resp4.text)

    json_resp = json.loads(resp4.text)
    exc_number= json_resp["meta"]["total"] 
    print("Number of Exclusion Sets:", exc_number)

    for i in range(exc_number):
        print('-', i,'Name of Exclusion Sets:', json_resp['data'][i]["name"], ', Operating System:',json_resp['data'][i]["operatingSystem"])

