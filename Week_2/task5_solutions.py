#Question1
#Prompt user for their 3 most favourite foods
first_food = input('Enter your first favourite food: ')
second_food = input('Enter your second favourite food: ')
third_food = input('Enter your third favourite food: ')

#Create tuple from inputs above
tuple = (first_food, second_food, third_food)
#Display tuple
print(tuple)
#Display tuple contents on new lines
print('\n'.join(tuple))

#Question2
#Ask for five best friends' names
first_friend = input('Enter your first friend\'s name here: ')
second_friend = input('Enter your second friend\'s name here: ')
third_friend = input('Enter your third friend\'s name here: ')
fourth_friend = input('Enter your fourth friend\'s name here: ')
fifth_friend = input('Enter your fifth friend\'s name here: ')

#Create a tuple from inputs above 
friends = (first_friend, second_friend, third_friend, fourth_friend, fifth_friend)
#Display results
print(friends[::-1])

#Question3
#Prompt user for five states 
first_state = input('Enter your first state: ')
second_state = input('Enter your second state: ')
third_state = input('Enter your third state: ')
fourth_state = input('Enter your fourth state: ')
fifth_state = input('Enter your fifth state: ')

#Create a tuple from data above
state_tuple = (first_state, second_state, third_state, fourth_state, fifth_state)
#Print first and last item in the tuple
print(state_tuple[0], state_tuple[-1])
#Check if Lagos is in tuple
print('Lagos' in state_tuple)
#Display number of states in tuple
print(len(state_tuple))

#Question4
#Prompt user for information like first name, age, e.t.c
first_name = input('Enter your first name here: ')
Age = int(input('Enter your age here: '))
color = input('Enter your favourite color here: ')
town = input('Enter your home town here: ')

#Create a tuple
info_tuple = tuple([first_name, Age, color, town])
#Unpack tuple
first_name, Age, color, town = info_tuple
#Display info on different lines
print(f'{first_name}\n{Age}\n{color}\n{town}')

#Question5
#Prompt user for info
first_item = input('Enter first item here: ')
second_item = input('Enter second item here: ')
third_item = input('Enter third item here: ')

#Create tuple
shopping_list = tuple([first_item, second_item, third_item])
#Convert tuple to list
shopping_list = list(shopping_list)

#Prompt for more info
fourth_item = input('Enter fourth item here: ')
fifth_item = input('Enter fifth item here: ')

#Append to list
shopping_list.append(fourth_item)
shopping_list.append(fifth_item)

#Convert to tuple
shopping_list = tuple(shopping_list)

#Print formatted output
print('|'.join(shopping_list))


#Question 6
#Create days_of_weeks and months_of_theyear tuples
days_of_weeks_tuple = tuple(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
months_of_the_year = tuple(['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

#Prompt user for information
name = input('Enter student\'s name: ')
gender = input('Enter student\'s gender: ')
course_track = input('Enter student\'s current track: ')
current_month = int(input('Enter current month\'s number'))
current_day_num = int(input('Enter current day\'s number'))

#Print output above
print(days_of_weeks_tuple)
print(months_of_the_year)
print(f'{name} \n {gender} \n {course_track} \n {current_month} \n {current_day_num}')

