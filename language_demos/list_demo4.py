class Person:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __repr__(self):
    return self.first_name + " " + self.last_name

people = [
  Person("Bob", "Smith"),
  Person("Sally", "Jones"),
  Person("Abby", "Timmons"),
  Person("Margrit", "Zimmerman"),
  Person("Olivia", "Rice"),
  Person("Sarah", "Gallie"),
]

print(people)

# people.sort(key=lambda p: p.last_name)
# print(people)

print(sorted(people, key=lambda p: p.last_name))
  