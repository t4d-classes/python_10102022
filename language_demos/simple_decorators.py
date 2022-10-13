

def wrapper(fn):
  def inner(*args, **kwargs):
    print("called from inner")
    return fn(*args, **kwargs)

  return inner

@wrapper
def do_it(a, b):
  return a + b

# wrapped_do_it = wrapper(do_it)


print(do_it(1,2))