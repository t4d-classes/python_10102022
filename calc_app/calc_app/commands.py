from calc_app.user_input import input_operand, input_entry_id
from calc_app.user_output import output_result
from calc_app.history import get_next_id, calc_result

def command_perform_math(history, command_name):
    operand = input_operand()
    history.append({
        "id": get_next_id(history),
        "command": command_name,
        "operand": operand
    })
    output_result(calc_result(history))
    return history

def command_print_history(history):
    for entry in history:
        print(entry)

def command_remove_history_entry(history):
    entry_id = input_entry_id()
    for entry in history:
        if entry["id"] == entry_id:
              history.remove(entry)
    return history

def command_clear():
    output_result(0)
    return []

def command_show_result(history):
    output_result(calc_result(history))
