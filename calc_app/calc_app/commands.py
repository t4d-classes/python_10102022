""" commands module """

from calc_app.user_input import input_operand, input_entry_id
from calc_app.user_output import output_result
from calc_app.history import get_next_id, calc_result, HistoryEntry

def command_perform_math(
    history: list[HistoryEntry],
    command_name: str) -> list[HistoryEntry]:
    """ command perform math """

    operand = input_operand()
    history.append({
        "id": get_next_id(history),
        "command": command_name,
        "operand": operand
    })
    output_result(calc_result(history))
    return history

def command_print_history(history: list[HistoryEntry]) -> None:
    """ command print history """

    for entry in history:
        print(entry)

def command_remove_history_entry(
    history: list[HistoryEntry]) -> list[HistoryEntry]:
    """ command remove history entry """

    entry_id = input_entry_id()
    for entry in history:
        if entry["id"] == entry_id:
            history.remove(entry)
    return history

def command_clear() -> list[HistoryEntry]:
    """ command clear """

    output_result(0)
    return []

def command_show_result(history: list[HistoryEntry]) -> None:
    """ command show result """

    output_result(calc_result(history))
