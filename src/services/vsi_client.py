# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import List, Optional

from dtos import VSI
from services.commands import (
    CommandResult,
    IBMVPCClient,
    ListVSICommand,
    StartVSICommand,
    StopVSICommand,
)


class VSIController:
    """
    High-level interface for controlling IBM Cloud Virtual Server Instances.
    """

    def __init__(self, region: str = "us-south"):
        # Set up the singleton only once
        IBMVPCClient(region)  # initializes the singleton, region must be passed

    def list_vsi(self) -> CommandResult[List[VSI]]:
        """
        List all VSIs in the specified zone.

        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with list of VSI DTOs
        """
        command = ListVSICommand()
        return command.execute()

    def start_vsi(self, vsi_id: str) -> CommandResult[Optional[str]]:
        """
        Start a VSI by its ID.

        :param vsi_id: ID of the VSI to start
        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with optional success message
        """
        command = StartVSICommand(vsi_id=vsi_id)
        return command.execute()

    def stop_vsi(self, vsi_id: str) -> CommandResult[Optional[str]]:
        """
        Stop a VSI by its ID.

        :param vsi_id: ID of the VSI to stop
        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with optional success message
        """
        command = StopVSICommand(vsi_id=vsi_id)
        return command.execute()
