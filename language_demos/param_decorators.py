
class App:

  __routes = {}

  def route(self, path):
    def wrapper(fn):
        self.__routes[path] = fn
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        return inner
    return wrapper

app = App()


@app.route("/do_it")
def do_it(a, b):
  return a + b

# wrapped_do_it = wrapper(do_it)


print(do_it(1,2))