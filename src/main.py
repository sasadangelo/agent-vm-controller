# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from typing import List

from dtos import VSI
from services import CommandResult, VSIController


def print_vsi_list(vsi_list: List[VSI]) -> None:
    """Prints the list of VSI objects in a human-readable format."""
    print(f"Retrieved {len(vsi_list)} VSI(s):")
    for vsi in vsi_list:
        print(
            f"- ID: {vsi.id}, Name: {vsi.name}, Status: {vsi.status}, Zone: {vsi.zone}, "
            f"CPU: {vsi.cpu}, RAM: {vsi.ram}MB"
        )


def main() -> None:
    controller = VSIController()

    # List all VSIs
    list_result_1: CommandResult[List[VSI]] = controller.list_vsi()

    if list_result_1.success and list_result_1.data:
        print_vsi_list(list_result_1.data)
    else:
        print(f"❌ Failed to retrieve VSI list: {list_result_1.message}")
        return

    # Optional: Find a VSI by name and stop/start it
    target_name = "test-vm"
    vsi = next((v for v in list_result_1.data if v.name == target_name), None)

    if not vsi:
        print(f"⚠️  VSI with name '{target_name}' not found.")
        return

    # Stop the VSI
    stop_result = controller.stop_vsi(vsi_id=vsi.id, zone=vsi.zone)
    print(f"🛑 Stop result: {stop_result.message}")

    # Start the VSI again
    start_result = controller.start_vsi(vsi_id=vsi.id, zone=vsi.zone)
    print(f"🚀 Start result: {start_result.message}")

    # List all VSIs
    list_result_2: CommandResult[List[VSI]] = controller.list_vsi()

    if list_result_2.success and list_result_2.data:
        print_vsi_list(list_result_2.data)
    else:
        print(f"❌ Failed to retrieve VSI list: {list_result_2.message}")
        return


if __name__ == "__main__":
    main()
