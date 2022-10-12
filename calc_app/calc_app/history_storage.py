""" history storage abstract class module """

from abc import ABC, abstractmethod

from .history import History


class HistoryStorage(ABC):
    """ history storage abstract class """

    @abstractmethod
    def load(self, history: History) -> None:
        """ load history """

    @abstractmethod
    def save(self, history: History) -> None:
        """ save history"""
