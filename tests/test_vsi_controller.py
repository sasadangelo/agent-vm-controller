# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
import unittest
from typing import List

from dtos import VSI
from services import CommandResult, VSIController


class TestVSIController(unittest.TestCase):
    def setUp(self):
        # Instantiate the controller once for all tests
        self.controller = VSIController()
        self.zone = "us-south"  # Adjust this to your real zone

    def test_list_vsi(self):
        """Test listing VSI instances (requires at least one VSI to exist)."""
        result: CommandResult[List[VSI]] = self.controller.list_vsi(zone=self.zone)
        self.assertTrue(result.success, msg=f"List failed: {result.message}")
        self.assertIsInstance(result.data, list)
        self.assertGreater(len(result.data), 0, "Expected at least one VSI in the list.")

    def test_stop_start_vsi(self):
        """Test stopping and starting a VSI by ID (assumes a 'test-vm' exists)."""
        list_result: CommandResult[List[VSI]] = self.controller.list_vsi(zone=self.zone)
        self.assertTrue(list_result.success, msg=f"List failed: {list_result.message}")
        self.assertIsNotNone(list_result.data)

        # Find VSI by name
        vsi = next((v for v in list_result.data if v.name == "test-vm"), None)
        self.assertIsNotNone(vsi, "VSI named 'test-vm' not found.")

        # Stop VSI
        stop_result = self.controller.stop_vsi(vsi_id=vsi.id, zone=vsi.zone)
        self.assertTrue(stop_result.success, msg=f"Stop failed: {stop_result.message}")

        # Start VSI
        start_result = self.controller.start_vsi(vsi_id=vsi.id, zone=vsi.zone)
        self.assertTrue(start_result.success, msg=f"Start failed: {start_result.message}")

    def test_stop_invalid_vsi(self):
        """Test stopping a VSI with an invalid ID to trigger error handling."""
        invalid_id = "fake-vsi-id"
        result = self.controller.stop_vsi(vsi_id=invalid_id, zone=self.zone)
        self.assertFalse(result.success)
        self.assertIn("Failed", result.message)


if __name__ == "__main__":
    unittest.main()
