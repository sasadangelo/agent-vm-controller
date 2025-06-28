# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_vpc import VpcV1


class StartVSICommand:
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region

    def execute(self):
        load_dotenv()
        api_key = os.environ["API_KEY"]
        authenticator = IAMAuthenticator(api_key)
        vpc = VpcV1(authenticator=authenticator)
        vpc.set_service_url(f"https://{self.region}.iaas.cloud.ibm.com/v1")

        response = vpc.list_instances()
        if response.get_status_code() != 200:
            return f"Errore nel recupero delle VM: {response.get_result()}"

        for vsi in response.get_result()["instances"]:
            if vsi["name"] == self.name:
                instance_id = vsi["id"]
                break
        else:
            return f"VM '{self.name}' non trovata"

        resp = vpc.create_instance_action(instance_id=instance_id, type="start")
        if resp.get_status_code() == 201:
            return f"VM '{self.name}' avviata con successo."
        else:
            return f"Errore avvio: {resp.get_result()}"
