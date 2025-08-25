students = {'Ada': 85, 'John': 40, 'Musa': 65}

passed_students = {name: score for name, score in students.items() if score > 50}
print(passed_students)

student = {"name": "Ada", "age": 20, "course": "Computer Science"}
print(student.get('age'))

student.pop("age")
print(student)

student = {"name": "Ada", "age": [20,24,35], "course": "Computer Science"}
student.pop("age")
print(student)

student.update({'name': 'John', 'course': 'mathematics'})
print(student)

student.update({'name': 'Stephen'})
print(student)