import json
import mysql.connector
from whoisapi import *
import requests

######################################################
## global variables
######################################################

global url
global responseglobal 
global domains_lst
# full_api_url = https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_XGGEvybXDmcdBvTnBiNbQyGQekz6i&domainName=google.com
apiKey = 'at_XGGEvybXDmcdBvTnBiNbQyGQekz6i'


######################################################
# Account Details
######################################################
'''
username = 'gmm0812@protonmail.com'
password = 'who-CV$1012~rA'
domain = 'whoisxmlapi.com'
'''



######################################################
## parse domains from yml to list
######################################################

# domains_lst = ['google.com', 'apple.com', 'pfizer.com']

file_list = open('domains.yml')
domains_lst = []
for line in file_list:
    domains_lst.append(line.strip())
print(domains_lst)



######################################################
## notify email
######################################################

## use gmail API for email notifications
## https://pythongeeks.org/send-email-using-python/

def email_notify():

    print('sent notification')



######################################################
## loop list to execute whois commands
######################################################
i = 0
while i < len(domains_lst):
    print(domains_lst[i])
    url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService?' + 'domainName=' + domains_lst[i] + '&apiKey=' + apiKey + "&outputFormat=JSON"
    print(url)    
    response = requests.get(url)
    # print(response.json())

    ## Writing output to temp file for regex parsing
    f = open('tmp_'+domains_lst[i]+'_whois.txt', 'w')
    f.write(str(response.json()))
    f.close()
    i+=100
else:
    print('exiting')


