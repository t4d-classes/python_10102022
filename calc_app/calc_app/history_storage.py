""" history storage abstract class module """

from abc import ABC, abstractmethod

from .history import History


class HistoryStorage(ABC):
    """ history storage abstract class """

    @abstractmethod
    async def load(self, history: History) -> None:
        """ load history """

    @abstractmethod
    async def save(self, history: History) -> None:
        """ save history"""
