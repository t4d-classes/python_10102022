

result = 0

command = input("Enter a command > ")

while command:

  if command == "add":
    operand = int(input("Please enter an operand: "))
    result = result + operand
    print(result)
  elif command == "subtract":
    operand = int(input("Please enter an operand: "))
    result = result - operand
    print(result)
  elif command == "multiply":
    operand = int(input("Please enter an operand: "))
    result = result * operand
    print(result)
  elif command == "divide":
    operand = int(input("Please enter an operand: "))
    result = result / operand
    print(result)
  elif command == "clear":
    result = 0
    print(result)
  else:
    print("unknown command, please try again")



  command = input("Enter a command > ")