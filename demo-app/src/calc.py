
def input_command():
    return input("Enter a command > ")

def input_operand():
    return float(input("Please enter an operand: "))

def input_entry_id():
    return int(input("Please the id of the history entry to remove: "))

def output_result(r):
    print(f"Result: {r}")

def output_unknown_command():
    print("unknown command, please try again")

def command_perform_math(result, history, command_name, math_op):
    operand = input_operand()
    history.append({
        "id": get_next_id(history),
        "command": command_name,
        "operand": operand
    })
    result = math_op(result, operand)
    output_result(result)

    return (result, history)

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
    return (0, [])

def get_next_id(history):
    if len(history) == 0:
      return 1
    ids = [ entry["id"] for entry in history ]
    return max(ids) + 1

def app():

  result = 0
  history = []

  math_ops = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
  }

  command = input_command()

  while command:
      if (command in math_ops):
          result, history = command_perform_math(result, history, command, math_ops[command])
      elif command == "clear":
          result, history = command_clear()
      elif command == "history":
          command_print_history(history)
      elif command == "remove":
          history = command_remove_history_entry(history)
      else:
          output_unknown_command()

      command = input_command()


app()