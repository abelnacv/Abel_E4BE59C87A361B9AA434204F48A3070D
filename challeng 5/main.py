def sort_students(students):
  students.sort(key=lambda student: student.cgpa, reverse=True)

class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

students = [
  Student("Alice", "001", 3.8),
  Student("Bob", "002", 3.5),
  Student("Charlie", "003", 3.9),
]

sort_students(students)

for student in students:
  print(student.name, student.roll_number, student.cgpa)