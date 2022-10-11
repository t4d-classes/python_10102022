math_ops = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}


def calc_result(history):
  result = 0
  for entry in history:
    math_op = math_ops[entry["command"]]
    result = math_op(result, entry["operand"])
  return result



def get_next_id(history):
    if len(history) == 0:
      return 1
    ids = [ entry["id"] for entry in history ]
    return max(ids) + 1
