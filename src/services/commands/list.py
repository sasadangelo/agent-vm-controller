# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import List

from dtos import VSI
from services.commands.base import BaseCommand, CommandResult
from services.commands.ibm_vpc_client import IBMVPCClient


class ListVSICommand(BaseCommand):
    def __init__(self):
        """
        Initialize with the IBM Cloud zone (availability zone).

        :param zone: IBM Cloud zone (e.g., "us-south-1").
        """
        # Instantiate the VPC client for the given zone
        self.vpc_client = IBMVPCClient().get_client()

    def execute(self) -> CommandResult[List[VSI]]:
        """
        List VSIs in the specified zone.

        :return: CommandResult with list of VSI DTOs on success,
                 or error message on failure.
        """
        # Make a request to the IBM Cloud VPC API to list all instances
        response = self.vpc_client.list_instances()
        # Check if the API call was successful
        if response.get_status_code() != 200:
            # Return a failure result with the error message
            return CommandResult(
                success=False,
                message=f"Error listing VMs: {response.get_result()}",
                data=None,
            )
        # Extract the list of instance dictionaries from the response
        instances = response.get_result().get("instances", [])
        # Convert each instance dictionary into a VSI DTO
        vsi_list = [
            VSI(
                id=vsi["id"],
                name=vsi["name"],
                status=vsi["status"],
                zone=vsi.get("zone", {}).get("name", "N/A"),
                cpu=vsi.get("vcpu", {}).get("count", 0),
                ram=vsi.get("memory", 0),
            )
            for vsi in instances
        ]
        # Return a successful CommandResult containing the list of VSI objects
        return CommandResult(
            success=True,
            message="VM list retrieved successfully.",
            data=vsi_list,
        )
