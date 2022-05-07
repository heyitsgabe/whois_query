import json
import mysql.connector
from whoisapi import *
import requests

######################################################
## global variables
######################################################

global url
global response
# full_api_url = https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_XGGEvybXDmcdBvTnBiNbQyGQekz6i&domainName=google.com
apiKey = 'at_XGGEvybXDmcdBvTnBiNbQyGQekz6i'

'''
client = Client(api_key=at_XGGEvybXDmcdBvTnBiNbQyGQekz6i)

#getting parsed whois record as a model instance. 
whois = client.data('whoisxmlapi.com')
print(whois.created_date_raw)

# Get raw API response
resp_str = client.raw_data('whoisxmlapi.com')
'''

'''
url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'

######################################################
# Account Details
######################################################

username = 'gmm0812@protonmail.com'
password = 'who-CV$1012~rA'
domain = 'whoisxmlapi.com'
'''



'''
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

domainName = 'pfizer.com'
apiKey = 'at_XGGEvybXDmcdBvTnBiNbQyGQekz6i'

url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?'\
    + 'domainName=' + domainName + '&apiKey=' + apiKey + "&outputFormat=JSON"

print(urlopen(url).read().decode('utf8'))
'''



######################################################
## parse domains from yml to list
######################################################
global domains_lst
# domains_lst = ['google.com', 'apple.com', 'pfizer.com']

file_list = open('domains.yml')
domains_lst = []
for line in file_list:
    domains_lst.append(line.strip())
print(domains_lst)


######################################################
## loop list to execute whois commands
######################################################
i = 0
while i < len(domains_lst):
    print(domains_lst[i])
    url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?' + 'domainName=' + domains_lst[i] + '&apiKey=' + apiKey + "&outputFormat=JSON"
    print(url)    
    response = requests.get(url)
    print(response.json())
    i+=100
else:
    print('exiting')



######################################################
## test get request for connection
######################################################

# response = requests.get(url)
# print(response.status_code)
# print(response.json())

######################################################
## notify email
######################################################

## use gmail API for email notifications