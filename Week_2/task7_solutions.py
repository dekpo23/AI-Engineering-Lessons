#Question 1
name = input('Enter your name here: ')
age = int(input('Enter student\'s age here: '))
gender = input('Enter student\'s gender here: ')
courses = input('Enter your courses seperated by space here: ')

student_bio = {}
student_bio['Student Name'] = name
student_bio['age'] = age
student_bio['gender'] = gender
student_bio['courses'] = courses.split()
courses_fmt = ' '.join(student_bio['courses'])



print(f'name: {student_bio["Student Name"]:>44} \nage: {student_bio["age"]:>45} \ngender: {student_bio["gender"]:>42} \ncourses: {courses_fmt:>41}')


#Question 2
items = ['books', 'pen', 'charger']

price1 = float(input('Enter price for item 1: '))
price2 = float(input('Enter price for item 2: '))
price3 = float(input('Enter price for item 3: '))

dic = {}
dic[items[0]] = price1
dic[items[1]] = price2
dic[items[2]] = price3

print(list(dic.keys()))
print(list(dic.values()))

change_item = input('Enter item which price you want to update: ')
change_price = float(input('Enter updated price here: '))
print(change_item in dic.keys())

dic.update({change_item: change_price})
print(dic)


#Question 3
days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
day1 = input('Enter first day of the week where you perform an activity: ')
day2 = input('Enter second day of the week where you perform an activity: ')
day3 = input('Enter third day of the week where you perform an activity: ')

activity1 = input('Enter first activity: ')
activity2 = input('Enter second activity: ')
activity3 = input('Enter third activity: ')

active_days_tuple = (day1, day2, day3)
activities = (activity1, activity2, activity3)
print({day: activity for day, activity in zip(active_days_tuple, activities)})


#Question 4
names = input('Enter 3 names seperated by comma here: ')
names_set = set(names.split(','))
names_set = set(name.strip() for name in names_set)
names_dic = {name: len(name) for name in names_set}
print(names_dic)

#Question 5
names = ('David', 'Ekpo', 'Friday')
phone_nos = ('915556', '081699', '905067')
info = {name: num for name, num in zip(names, phone_nos)}
new_name = input('Enter a name: ')
print(info.get(new_name))


#Collect Basic Info
name = input('Enter student\'s name here: ')
age = int(input('Enter student\'s age here: '))
gender = input('Enter student\'s gender here: ')
class_ = input('Enter student\'s class here: ')

#Collect scores for subjects
subjects = ('maths', 'eng', 'bio', 'chem', 'phy')

scores = tuple(float(input(f'Enter score for {subject}: ')) for subject in subjects)

#Guardian info
Guardian_name = input('Enter guardian name here: ')
Guardian_phone_num = input('Enter guardian phone number here: ')

#hobbies
hobbies = set(input('Enter hobbies seperated by commas: ').split(','))
hobbies = tuple(hobby.strip() for hobby in hobbies)

class_profile = {'Basic Info': {'Name': name.title(), 'Age': age, 'class': class_, 'Gender': gender}, 'Performance': {subject: score for subject, score in zip(subjects, scores)}, 'Guardian info': {'Guardian name': Guardian_name.title(), 'Guardian Phone number': Guardian_phone_num}, 'Hobbies': list(hobbies)}

#Derived Data
class_profile["Performance"]["Average"] = sum(scores) / len(scores)
class_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
class_profile["Hobbies Count"] = len(hobbies)

#Output
title = 'Student Profile'
title2 = 'Student\'s Performance'
title3 = 'Guardian Information'
title4 = 'Hobbies'


print('\n')
print(f'{title:^50}')
print(f"Name: {class_profile['Basic Info']['Name']:>44}")
print(f"Age: {class_profile['Basic Info']['Age']:>45}")
print(f"Gender: {class_profile['Basic Info']['Gender']:>42}")

print('\n')
print(f'{title2:^50}')
print(class_profile["Performance"])

print('\n')
print(f'{title3:^50}')
print(class_profile["Guardian info"])

print('\n')
print(f'{title4:^50}')
print(class_profile["Hobbies"])
print(f"\nTotal Hobbies:\t{class_profile['Hobbies Count']}")
print(f"Average Score:\t{class_profile['Performance']['Average']:.2f}")







