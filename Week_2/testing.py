#Question4
#Prompt user for information like first name, age, e.t.c
first_name = input('Enter your first name here: ')
Age = int(input('Enter your age here: '))
color = input('Enter your favourite color here: ')
town = input('Enter your home town here: ')

#Create a tuple
info_tuple = tuple([first_name, Age, color, town])
#Unpack tuple
name, colour, age, town = info_tuple
#Display info on different lines
#rint(f'{first_name}\n{Age}\n{color}\n{town}')
print(name)
print(info_tuple)
print(colour)