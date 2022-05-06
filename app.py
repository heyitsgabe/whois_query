import json
import mysql.connector
from whoisapi import *

'''
# api_key = at_XGGEvybXDmcdBvTnBiNbQyGQekz6i

client = Client(api_key=at_XGGEvybXDmcdBvTnBiNbQyGQekz6i)

#getting parsed whois record as a model instance. 
whois = client.data('whoisxmlapi.com')
print(whois.created_date_raw)

# Get raw API response
resp_str = client.raw_data('whoisxmlapi.com')
'''

url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'

######################################################
# Account Details
######################################################

username = 'gmm0812@protonmail.com'
password = 'who-CV$1012~rA'
domain = 'whoisxmlapi.com'
