# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import Optional

from services.commands.base import BaseCommand, CommandResult
from services.commands.ibm_vpc_client import IBMVPCClient


class StopVSICommand(BaseCommand):
    def __init__(self, vsi_id: str, zone: str):
        self.vsi_id = vsi_id
        # Instantiate the VPC client for the given zone
        self.vpc_client = IBMVPCClient(zone).get_client()

    def execute(self) -> CommandResult[Optional[str]]:
        """
        Stops the VSI with the given ID in the specified region.

        Returns:
            CommandResult containing success status and optional message.
        """
        # Directly attempt to stop the VSI by ID
        try:
            # Attempt to send the stop action to the VSI instance
            resp = self.vpc_client.create_instance_action(instance_id=self.vsi_id, type="stop")
        except Exception as e:
            # Return a failure result with the exception message
            return CommandResult(False, message=f"Exception occurred while stopping VSI: {e}")
        # If the API call returns HTTP 201, the stop action succeeded
        if resp.get_status_code() == 201:
            return CommandResult(True, message=f"VSI '{self.vsi_id}' stopped successfully.")
        else:
            # Extract and return the error details from the response
            return CommandResult(False, message=f"Failed to stop VSI: {resp.get_result()}")
