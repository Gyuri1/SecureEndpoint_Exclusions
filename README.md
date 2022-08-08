# SecureEndpoint_Exclusions

This script will list exclusions of a Secure Endpoint Org.  
This script works in US / NAM Secure Endpoint Cloud.  

Please update 'Client_ID' and 'Client_Pass' values according to this doc in the script before execuring it:
https://developer.cisco.com/docs/secure-endpoint/#!authentication



How to run:
```
python3 secureendpoint_list_exclusion.py
SecureX Token was received
Secure Endpoint Token was received
Number of Orgs: 1
Name of the 1st Org: MyOwnOrg
Number of Exclusion Sets: 7
- 0 Name of Exclusion Sets: Exclusions For 'Initial FireAMP Windows Policy, FireAMP Windows' , Operating System: windows
- 1 Name of Exclusion Sets: Exclusions For Exploit Prevention Policy , Operating System: windows
- 2 Name of Exclusion Sets: Exclusions For Malicious Activity Protection Policy , Operating System: windows
- 3 Name of Exclusion Sets: KAS , Operating System: windows
- 4 Name of Exclusion Sets: TEST , Operating System: windows
- 5 Name of Exclusion Sets: Exclusions For 'Copy of Initial FireAMP Mac Policy, Mac' , Operating System: mac
- 6 Name of Exclusion Sets: Workstation Exclusions For FireAMP Linux , Operating System: linux
```
