""" history abstract class module """

from typing import Iterator
from abc import ABC, abstractmethod

class HistoryEntry:
    """ history entry dictionary """
    def __init__(self, history_entry_id: int, command: str, operand: float):
        self.history_entry_id = history_entry_id
        self.command = command
        self.operand = operand

    def __repr__(self) -> str:
        return (
            f"Id: {self.history_entry_id}"
            f", Command: {self.command}"
            f", Operand: {self.operand}"
        )

class History(ABC):
    """ history abstact class """

    @abstractmethod
    def append_entry(self, command_name: str, operand: float) -> None:
        """ append a history entry"""

    @abstractmethod
    def remove_entry(self, entry_id: int) -> None:
        """ remove a history entry by id """

    @abstractmethod
    def clear_entries(self) -> None:
        """ clear history entries """

    @abstractmethod
    def __iter__(self) -> Iterator[HistoryEntry]:
        ...

    @abstractmethod
    def __next__(self) -> HistoryEntry:
        ...
      