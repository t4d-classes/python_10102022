

result = 0

history = []

def get_next_id(history):

  if (len(history) == 0):
    return 1

  ids = [ entry["id"] for entry in history ]
  return max(ids) + 1


command = input("Enter a command > ")

while command:

  if command == "add":
    operand = int(input("Please enter an operand: "))
    history.append({
      "id": get_next_id(history), "command": "add", "operand": operand
    })
    result = result + operand
    print(result)
  elif command == "subtract":
    operand = int(input("Please enter an operand: "))
    history.append({
      "id": get_next_id(history), "command": "subtract", "operand": operand
    })
    result = result - operand
    print(result)
  elif command == "multiply":
    operand = int(input("Please enter an operand: "))
    history.append({
      "id": get_next_id(history), "command": "multiply", "operand": operand
    })
    result = result * operand
    print(result)
  elif command == "divide":
    operand = int(input("Please enter an operand: "))
    history.append({
      "id": get_next_id(history), "command": "divide", "operand": operand
    })
    result = result / operand
    print(result)
  elif command == "clear":
    result = 0
    history = []
    print(result)
  elif command == "history":
    for entry in history:
      print(entry)
  elif command == "remove":
    entryId = int(input("Please the id of the history entry to remove: "))
    for entry in history:
      if entry["id"] == entryId:
        history.remove(entry)
  else:
    print("unknown command, please try again")



  command = input("Enter a command > ")