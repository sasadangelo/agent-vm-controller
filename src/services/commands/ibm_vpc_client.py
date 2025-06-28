import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_vpc import VpcV1


class IBMVPCClient:
    _instance = None

    def __new__(cls, region: str = "us-south"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(region)
        return cls._instance

    def _init(self, region: str):
        load_dotenv()
        api_key = os.environ.get("API_KEY")
        if not api_key:
            raise ValueError("API_KEY not set in environment variables")
        authenticator = IAMAuthenticator(api_key)
        self.client = VpcV1(authenticator=authenticator)
        self.client.set_service_url(f"https://{region}.iaas.cloud.ibm.com/v1")

    def get_client(self) -> VpcV1:
        return self.client
