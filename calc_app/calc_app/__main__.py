from calc_app.user_input import input_command, input_operand, input_entry_id

math_ops = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

def output_result(result):
    print(f"Result: {result}")

def output_unknown_command():
    print("unknown command, please try again")

def calc_result(history):
  result = 0
  for entry in history:
    math_op = math_ops[entry["command"]]
    result = math_op(result, entry["operand"])
  return result


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

def get_next_id(history):
    if len(history) == 0:
      return 1
    ids = [ entry["id"] for entry in history ]
    return max(ids) + 1

def app():

  history = []

  command = input_command()

  while command:
      if (command in math_ops):
          history = command_perform_math(history, command)
      elif command == "clear":
          history = command_clear()
      elif command == "history":
          command_print_history(history)
      elif command == "remove":
          history = command_remove_history_entry(history)
      elif command == "result":
          command_show_result(history)
      else:
          output_unknown_command()

      command = input_command()


app()