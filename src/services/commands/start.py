# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import Optional

from services.commands.base import CommandResult
from services.commands.ibm_vpc_client import IBMVPCClient


class StartVSICommand:
    def __init__(self, vsi_id: str, zone: str):
        self.vsi_id = vsi_id
        self.vpc_client = IBMVPCClient(zone).get_client()

    def execute(self) -> CommandResult[Optional[str]]:
        """
        Start the VSI identified by vsi_id in the specified zone.

        Returns:
            CommandResult with success status and optional message.
        """
        # Directly attempt to start the VSI by ID
        try:
            # Attempt to send the stop action to the VSI instance
            resp = self.vpc_client.create_instance_action(instance_id=self.vsi_id, type="start")
        except Exception as e:
            # Return a failure result with the exception message
            return CommandResult(False, message=f"Exception occurred while starting VSI: {e}")
        # If the API call returns HTTP 201, the start action succeeded
        if resp.get_status_code() == 201:
            return CommandResult(True, message=f"VSI '{self.vsi_id}' started successfully.")
        else:
            # Extract and return the error details from the response
            return CommandResult(False, message=f"Failed to start VSI: {resp.get_result()}")
