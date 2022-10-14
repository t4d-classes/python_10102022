

# def get_nums():
#   print("call get nums")
#   return [ 1, 2, 3 ]

def get_nums():
  print("call get nums")
  yield 1
  print("resume get nums")
  yield 2
  print("resume get nums")
  yield 3


for num in get_nums():
  print("in the for-in loop", num)

nums = range(10)