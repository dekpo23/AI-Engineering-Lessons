names = ['Esther', 'Precious', 'Kennie']
scores = [85, 90, 75]
for i, j in zip(names, scores):
    print(i, "scored", j)


def greet():
    print('Hello, welcome to AI Fellowship!')

greet()
greet()
greet()

def greet(name):
    print("Hello", name, "welcome to Python learning!")

greet('Class Rep')
greet('Ridwan')

def greet(name):
    print('Hello', name)

result = greet('Esther')
print('Result: ', result)

def add(a, b):
    return  a + b
result = add(4, 6)
print('The sum is: ', result)

def count_up_to(n):
    i = 1
    while i < n:
        yield i
        i += 1
for number in count_up_to(5):
    print(number)

def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print('Sum:', total)

add_numbers(2, 4, 6)

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

student_details(name = 'Peter', track = 'AI Engineering', interest = 'Block Chain')


def participant_info(name, age, track = 'AI Engineering', *skills, **extra_info):
    """
    Generate profile
    """
    profile = f'\n-- Bootcamp Participant Profile ---\n'
    profile += f'Name: {name}\n'
    profile += f'Age: {age}\n'

    # Skills
    if skills:
        profile += 'Skills: ' + ', '.join(skills) + '\n'
    else:
        profile += 'Skills: Not yet specified\n'
    
    #Extra info
    if extra_info:
        profile += 'Additional Info:\n'
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"


    return profile

print(participant_info('Peter', 24))
print(participant_info('Ridwan', 29, track = 'AI Engineering'))
print(participant_info('David', 27, 'Data Science', 'Python', 'SQL', 'Machine Learning'))
print(participant_info('Sophia', 30, 'Cybersecurity', 'Networking',
                        'Ethical Hacking', 'Python', interest = 'Blockchain',
                        city = 'Sagamu', phone = '08123456789'))