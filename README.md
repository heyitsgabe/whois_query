# whois_query
Coding test: automated whois query

API calls are from https://whois.whoisxmlapi.com/ 

This is a Python script set to run every 24 hours scanning a list of domains. 

Domains are listed in the domains.yml file. 

command line arguments required on execution. Arguments are sender address, receiver address, and sender password. These arguments are meant for the email notification system. 

Email sending functions were tested on a testing gmail account.

Target data values are stored in dictionaries and compared to an initial and updated dictionary. If the values aren't equal notification email is sent.
