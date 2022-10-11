""" history module """

from collections.abc import Callable
from typing import TypedDict

class HistoryEntry(TypedDict):
    """ history entry dictionary """
    id: int
    command: str
    operand: float

math_ops: dict[str, Callable[[float, float], float]] = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

def calc_result(history: list[HistoryEntry]) -> float:
    """ calculate the current result from the history """
    result: float = 0
    for entry in history:
        math_op = math_ops[entry["command"]]
        result = math_op(result, entry["operand"])
    return result


def get_next_id(history: list[HistoryEntry]) -> int:
    """ get next id """
    if len(history) == 0:
        return 1
    ids = [ entry["id"] for entry in history]
    return max(ids) + 1
