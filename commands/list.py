# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
import os

import pandas as pd
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_vpc import VpcV1

from commands.base import BaseCommand


class ListVSICommand(BaseCommand):
    def __init__(self, region: str):
        self.region = region

    def execute(self):
        load_dotenv()
        api_key = os.environ["API_KEY"]
        authenticator = IAMAuthenticator(api_key)
        vpc = VpcV1(authenticator=authenticator)
        vpc.set_service_url(f"https://{self.region}.iaas.cloud.ibm.com/v1")

        response = vpc.list_instances()
        if response.get_status_code() != 200:
            return f"Errore nella lista delle VM: {response.get_result()}"

        instances = response.get_result()["instances"]

        data = []
        for vsi in instances:
            data.append(
                {
                    "ID": vsi["id"],
                    "Name": vsi["name"],
                    "Status": vsi["status"],
                    "Zone": vsi["zone"]["name"] if "zone" in vsi else "N/A",
                    "CPU": vsi["vcpu"]["count"] if "vcpu" in vsi else "N/A",
                    "RAM (GB)": vsi["memory"] if "memory" in vsi else "N/A",
                }
            )

        df = pd.DataFrame(data)
        return df
