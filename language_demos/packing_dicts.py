

person = { "fn": "Bob", "ln": "Smith" }
person_secure = { "ssn": "123-12-1234" }

# print(*person)
# print(*person.values())
# print(*person.items())

# for data in person:
#   print(data)

# print(list(person))

first, last = person

print(first, last)

# print({ **person, **person_secure })