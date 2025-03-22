#launch an ansible job using the Ansible Tower rest API
import os
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("Ansible_Host")
USERNAME = os.getenv("Ansible_Username")
PASSWORD = os.getenv("Ansible_Password")

def launch_ansible_job(template_id: int, extra_vars: dict):
    url = f"https://{HOST}/api/v2/job_templates/{template_id}/launch/"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "extra_vars": extra_vars
    }

    response = requests.post(url, auth=(USERNAME, PASSWORD), headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        job_details = response.json()
        return job_details
    else:
        return {"error": response.text}

