
# arguments are expressions whose result is passed into a function
# parameters are variables that are assigned the result of an argument's expression


def do_it(param1,  param2 = 888, *args, param3 = 999, **kwargs):
  print(param1, param2, param3, args, kwargs)


arg1 = [1,2,3]

# invoke
do_it(1,4,5,6,7, param3 = 3, param4 = 777, param5 = 666)

