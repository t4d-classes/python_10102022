""" history module """

from typing import Iterator

from .history import HistoryEntry, History


class HistoryList(History):
    """ history class"""

    __history: list[HistoryEntry]
    __current_iter: Iterator[HistoryEntry]

    def __init__(self) -> None:
        self.__history = []

    def __get_next_id(self) -> int:
        """ get next id """
        if len(self.__history) == 0:
            return 1
        ids = [ entry.history_entry_id for entry in self.__history]
        return max(ids) + 1

    def append_entry(self, command_name: str, operand: float) -> None:
        """ append a history entry"""
        self.__history.append(
            HistoryEntry(self.__get_next_id(), command_name, operand))

    def remove_entry(self, entry_id: int) -> None:
        """ remove a history entry by id """
        for entry in self.__history:
            if entry.history_entry_id == entry_id:
                self.__history.remove(entry)

    def clear_entries(self) -> None:
        """ clear history entries """
        self.__history = []

    def __iter__(self) -> Iterator[HistoryEntry]:
        self.__current_iter = iter(self.__history)
        return self.__current_iter

    def __next__(self) -> HistoryEntry:
        return next(self.__current_iter)
