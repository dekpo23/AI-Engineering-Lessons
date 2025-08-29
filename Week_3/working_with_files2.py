from pathlib import Path

workspace = Path('workspace_files')
workspace.mkdir(exist_ok=True)
file_path = workspace / 'notes.txt'

# f = open(file_path, "w", encoding = 'utf-8')
# f.write('This is the first line in notes.txt\n')

# f = open(file_path, 'w', encoding = 'utf-8')
# f.write('Replaced the old content with new content')
# f.close()

# f = open(file_path, 'w', encoding = 'utf-8')
# f.write('Shopping List:\n')
# f.write('- Rice')
# f.close()

# f = open(file_path, 'r', encoding = 'utf-8')
# print('First Line:', f.readline().rstrip())
# print('Second Line:', f.readline().rstrip())

# f = open(file_path, 'r', encoding='utf-8')
# for line in f:
#     print('->', line.rstrip())
# f.close()

# with open(file_path, 'w', encoding = 'utf-8')  as f:
#     f.write('My Todo List:\n')
#     f.write(' - Revise Python file handling\n')
#     f.write(' - Practise error handling within a function\n')

# with open(file_path, 'a', encoding ='utf-8') as f:
#     f.write('-Build a small project\n')

# from pathlib import Path
# workspace = Path('workspace_files')
# workspace.mkdir(exist_ok=True)

# try:
#     with open(workspace / 'missing_file.txt', 'r') as f:
#         content = f.read() 
#         print('File content:', content)
# except FileNotFoundError:
#     print('File does not exists')
#     with open(workspace / 'missing_file.txt', 'w') as f:
#         f.write('Now I Exist')
#     print('file created succesfully')

# from pathlib import Path

# workspace = Path('workspace_files')
# file_path = workspace / 'notes.txt'
# if file_path.exists():
#     print(f'Found the file: {file_path.name}')

#     file_size = file_path.stat().st_size
#     print(f'File size: {file_size} bytes')

#     with open(file_path, 'r', encoding='utf-8'):
#         content = f.read()
#         print(f'Content preview: {content[:50]}...') # First 50 characters

# else:
#     print(f'File {file_path.name} doesn\'t exist')
#     print('You might want to create it first!')

import json
from pathlib import Path

workspace = Path("workspace_files")

# Create some student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

json_file = workspace / 'student_data.json'
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(student_data, f, indent = 2 )

print('Student data saved to JSON file')

with open(json_file, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print(loaded_data)

import csv
from pathlib import Path

workspace = Path('workspace_files')
csv_file = workspace / 'students.csv'

students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)

    for row_number, row in enumerate(reader):
        if row_number == 0:
            print(f'Headers : {' | '.join(row)}')
            print('-' * 40)
        else:
            name, age, course, grade = row
            print(f'{name} ({age} years) {course}: {grade}')


