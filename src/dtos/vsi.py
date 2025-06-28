# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from dataclasses import dataclass


@dataclass
class VSI:
    """Data Transfer Object representing a Virtual Server Instance (VSI)."""

    id: str
    name: str
    status: str
    zone: str
    cpu: int
    ram: int
