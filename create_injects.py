import requests
from datetime import datetime
import pytz
import toml

login_url = "http://IP/api/login"
create_inject_url = "http://IP/api/injects/create"

config = toml.load("injects.conf")
injects = config.get('inject', [])

login_payload = {"username": "USERNAME", "password": "PASSWORD"}
session = requests.Session()
session = session = requests.session()

login_response = session = requests.post(login_url, json=login_payload)

if login_response.status_code != 200:
    raise Exception("Login failed")

pst = pytz.timezone('America/Los_Angeles')

for inject in config["inject"]:
    open_time = pst.localize(datetime.strptime(inject["open_time"], "%Y-%m-%d %H:%M")).astimezone(pytz.utc).isoformat()
    due_time = pst.localize(datetime.strptime(inject["due_time"], "%Y-%m-%d %H:%M")).astimezone(pytz.utc).isoformat()
    close_time = pst.localize(datetime.strptime(inject.get("close_time", inject["due_time"]), "%Y-%m-%d %H:%M")).astimezone(pytz.utc).isoformat()

    form_data = {
        "title": inject["title"],
        "description": inject.get("description", "See attached files."),
        "open-time": open_time,
        "due-time": due_time,
        "close-time": close_time,
    }

    files = inject.get("files", [])
    files = [("files", (file, open(file, 'rb'))) for file in files]

    response = requests.post(create_inject_url, data=form_data, files=files, cookies=login_response.cookies)

    for _, f in files:
        f[1].close()

    if response.status_code == 201:
        print(f"Successfully created inject: {inject['title']}")
    else:
        print(f"Failed to create inject: {inject['title']} - Status code: {response.status_code}")
