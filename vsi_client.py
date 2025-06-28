# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from commands.list import ListVSICommand
from commands.start import StartVSICommand
from commands.stop import StopVSICommand


class VSI:
    def __init__(self):
        # eventuale contesto o configurazione condivisa
        pass

    def list_vsi(self, region: str = "us-south"):
        command = ListVSICommand(region=region)
        return command.execute()

    def start_vsi(self, name: str, region: str = "us-south"):
        command = StartVSICommand(name=name, region=region)
        return command.execute()

    def stop_vsi(self, name: str, region: str = "us-south"):
        command = StopVSICommand(name=name, region=region)
        return command.execute()
