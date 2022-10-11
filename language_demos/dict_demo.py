person = {
  "first_name": "Bob",
  "last_name": "Smith",
  "age": 23
}

print(person["first_name"])

print("first_name" in person)

for key in person:
  print(key)

print(list(person))

print(person.keys())

print(person.values())

print(person.items())

for (key, value) in person.items():
    print(key + "=" + str(value))

for key in person:
  print(key + "=" + str(person[key]))

del person["last_name"]

print(person)

# print(person["last_name"])
print(person.get("last_name"))
print(person.get("last_name", "Timmons"))

print("last_name" not in person)
