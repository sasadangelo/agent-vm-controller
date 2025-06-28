# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import List, Optional

from dtos import VSI
from services.commands import (
    CommandResult,
    ListVSICommand,
    StartVSICommand,
    StopVSICommand,
)


class VSIController:
    """
    High-level interface for controlling IBM Cloud Virtual Server Instances.
    """

    def list_vsi(self, zone: str = "us-south") -> CommandResult[List[VSI]]:
        """
        List all VSIs in the specified zone.

        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with list of VSI DTOs
        """
        command = ListVSICommand(zone=zone)
        return command.execute()

    def start_vsi(self, vsi_id: str, zone: str = "us-south") -> CommandResult[Optional[str]]:
        """
        Start a VSI by its ID.

        :param vsi_id: ID of the VSI to start
        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with optional success message
        """
        command = StartVSICommand(vsi_id=vsi_id, zone=zone)
        return command.execute()

    def stop_vsi(self, vsi_id: str, zone: str = "us-south") -> CommandResult[Optional[str]]:
        """
        Stop a VSI by its ID.

        :param vsi_id: ID of the VSI to stop
        :param zone: IBM Cloud zone (default: "us-south")
        :return: CommandResult with optional success message
        """
        command = StopVSICommand(vsi_id=vsi_id, zone=zone)
        return command.execute()
