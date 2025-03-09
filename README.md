# Quotient-Injects
Small utility script to import injects from a configuration file for the Quotient scoring engine. 

> Times are configured to be in PST, change this in line 21 of the script:
```python
pst = pytz.timezone('America/Los_Angeles')
```

> Quotient IP and credentials can be changed in lines 6-7 and 12, respectively:
```python
login_url = "http://IP/api/login"
create_inject_url = "http://IP/api/injects/create"

login_payload = {"username": "USERNAME", "password": "PASSWORD"}
```