import json
from venv import create
from whoisapi import *
import requests
import os
from time import sleep
import re
import smtplib
import sys

global url
global responseglobal 
global domains_lst
global domains_val
global domains_val_update
global dict_initial
global dict_update

apiKey = 'at_XGGEvybXDmcdBvTnBiNbQyGQekz6i'
domains_lst = []
domains_val = []
domains_val_update = []
dict_initial = {}
dict_update = {}

file_list = open('domains.yml')
domains_lst = []
for line in file_list:
    domains_lst.append(line.strip())
print(domains_lst)



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
    i+=1
else:
    print('exiting whois scan...')



print('create inital dictionary.....')
domains_val = []
i=0
while i < len(domains_lst):
    file_val = open('tmp_'+domains_lst[i]+'_whois.txt', 'r')
    txt = str(file_val.read())
    file_val.close()

    ## regex for the target values
    created_match = re.findall("'createdDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
    updated_match = re.findall("'updatedDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
    expires_match = re.findall("'expiresDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)

    ## appending to the values list
    domains_val.append(created_match[0])
    domains_val.append(updated_match[0])
    domains_val.append(expires_match[0])

    i+=1

dict_initial = dict.fromkeys(domains_lst, domains_val)




print('create update dictionary.....')
domains_val_update = []
i=0
while i < len(domains_lst):
    file_val = open('tmp_'+domains_lst[i]+'_whois.txt', 'r')
    txt = str(file_val.read())
    file_val.close()

    ## regex for the target values
    created_match = re.findall("'createdDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
    updated_match = re.findall("'updatedDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
    expires_match = re.findall("'expiresDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)

    ## appending to the values list
    domains_val_update.append(created_match[0])
    domains_val_update.append(updated_match[0])
    domains_val_update.append(expires_match[0])

    i+=1

dict_update = dict.fromkeys(domains_lst, domains_val_update)

if dict_initial == dict_update:
    print('dictonaries are equal.....')
else:
    print('dictonaries are not equal.....')

    d=0
    while d < len(domains_lst):
        if dict_initial.get(domains_lst[d]) == dict_update.get(domains_lst[d]):
            print('equal value compare')
        else:
            print('not equal value compare')
            e = open('tmp_email_notify.txt', 'a')
            e.write('The following value has changed --- ' + domains_lst[d] + ': ' + dict_update.get(domains_lst[d]))
            e.close()

    d+=1

    print('sending email notification.....')

    sender_add = sys.argv[0]
    receiver_add = sys.argv[1]
    password = sys.argv[2] 
    
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()

    smtp_server.starttls()
    smtp_server.ehlo()

    smtp_server.login(sender_add, password)

    tmp_eml = open('tmp_email_notify.txt', 'r')
    msg = str(tmp_eml.read())
    tmp_eml.close()

    smtp_server.sendmail(sender_add, receiver_add, msg)
    
    print('message is sent.....')

    if os.path.exists('tmp_email_notify.txt'):
        os.remove('tmp_email_notify.txt')
    else:
        print('files deleted')

    smtp_server.quit()

dict_initial = dict_update



i=0
while i < len(domains_lst):
    if os.path.exists('tmp_'+domains_lst[i]+'_whois.txt'):
        os.remove('tmp_'+domains_lst[i]+'_whois.txt')
        i+=1
    else:
        print('files deleted')
else:
    print('tmp files deleted')
i+=1

print('sleeping.....')
## sleep for 24 hours
sleep(60 * 60 * 24)

r = 0
while r < 1:
    ## whois_scan
    print('begin whois scan.....')
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
        i+=1
    else:
        print('exiting whois scan...')

    ## create_update_dict()
    print('create update dictionary.....')
    domains_val_update = []
    i=0
    while i < len(domains_lst):
        file_val = open('tmp_'+domains_lst[i]+'_whois.txt', 'r')
        txt = str(file_val.read())
        file_val.close()

        ## regex for the target values
        created_match = re.findall("'createdDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
        updated_match = re.findall("'updatedDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)
        expires_match = re.findall("'expiresDate': '" + "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", txt)

        ## appending to the values list
        domains_val_update.append(created_match[0])
        domains_val_update.append(updated_match[0])
        domains_val_update.append(expires_match[0])

        i+=1

    dict_update = dict.fromkeys(domains_lst, domains_val_update)

    print('comparing dictionaries.....')

    if dict_initial == dict_update:
        print('dictonaries are equal.....')
    else:
        print('dictonaries are not equal.....')
        print('comparing values.....')
        
        d=0
        while d < len(domains_lst):
            if dict_initial.get(domains_lst[d]) == dict_update.get(domains_lst[d]):
                print('equal value compare')
            else:
                print('not equal value compare')
                e = open('tmp_email_notify.txt', 'a')
                e.write('The following value has changed --- ' + domains_lst[d] + ': ' + dict_update.get(domains_lst[d]))
                e.close()

        d+=1

        print('sending email notification.....')

        sender_add = sys.argv[0]
        receiver_add = sys.argv[1]
        password = sys.argv[2] 
        
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()

        smtp_server.starttls()
        smtp_server.ehlo()

        smtp_server.login(sender_add, password)

        tmp_eml = open('tmp_email_notify.txt', 'r')
        msg = str(tmp_eml.read())
        tmp_eml.close()

        smtp_server.sendmail(sender_add, receiver_add, msg)
        
        print('message is sent.....')

        if os.path.exists('tmp_email_notify.txt'):
            os.remove('tmp_email_notify.txt')
        else:
            print('files deleted')

        smtp_server.quit()

    ## refresh_dictionary()
    dict_initial = dict_update

    ## del_tmp_files()
    i=0
    while i < len(domains_lst):
        if os.path.exists('tmp_'+domains_lst[i]+'_whois.txt'):
            os.remove('tmp_'+domains_lst[i]+'_whois.txt')
            i+=1
        else:
            print('files deleted')
    else:
        print('tmp files deleted')
    i+=1

    sleep(10)



print('exiting script.....')