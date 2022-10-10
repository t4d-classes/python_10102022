# Explore Data Types

some_var = None
print(type(some_var))

some_var = 2
print(type(some_var))

some_var = 5.6
print(type(some_var))

some_var = "hello, world!"
print(type(some_var))

# print(1 + "hello")
# print(1 + 1.0)

some_var = False
print(type(some_var))

some_var = (1, 'fun', True)
print(type(some_var))
print(some_var[1])

# some_var[1] = "not fun"

some_var = [1,2,3,4,5]
print(type(some_var))

some_var = {
  "firstName": "Bob",
  "lastName": "Smith"
}
print(type(some_var))
print(some_var["firstName"])

def do_it():
  print("did it")

do_it()

some_var = do_it
print(type(some_var))


some_var = int("23")
print(type(some_var))

print("my favorite number is " + str(8))


print(bool((1,2)))


