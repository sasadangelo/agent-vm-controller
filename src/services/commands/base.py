# Copyright (c) 2025 Salvatore D'Angelo
# Author: Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo
# License: MIT
from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class CommandResult(Generic[T]):
    def __init__(self, success: bool, message: str = "", data: Optional[T] = None):
        self.success = success
        self.message = message
        self.data = data


class BaseCommand(ABC, Generic[T]):
    @abstractmethod
    def execute(self) -> CommandResult[T]:
        pass
