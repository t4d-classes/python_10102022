class Person:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def full_name(self):
    return self.first_name + " " + self.last_name


class Student(Person):
  
  def __init__(self, student_id, first_name, last_name):
    super().__init__(first_name, last_name)
    # Person.__init__(self, first_name, last_name)
    self.student_id = student_id

  def record_info(self):
    return f"{self.student_id} "\
      f"{self.last_name}, "\
      f"{self.first_name}"

class Instructor(Person):
  
  def __init__(self, supervisor_id, first_name, last_name):
    super().__init__(first_name, last_name)
    # Person.__init__(self, first_name, last_name)
    self.supervisor_id = supervisor_id

  def org_info(self):
    return (
      "Supervisor Id: "
      f"{self.supervisor_id} "
      ", Employee Name: "
      f"{self.last_name}, "
      f"{self.first_name}"
    )



student = Student(1, "Bob", "Smith")
print(student.full_name())
print(student.record_info())

instructor = Instructor(2, "Alice", "Thomas")
print(instructor.full_name())
print(instructor.org_info())
