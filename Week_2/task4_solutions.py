#Question 1

#Prompt user for favourite quote
quote = input('Enter your favourite quote here: ')
#Convert the quote to titled case
titled_quote = quote.title()
#Put the quotes in between quotation marks
print(f"\"{titled_quote}\"")

#Question 2
#Create empty list
empty_list = []
#Prompt user for first item
item1 = input('Enter first item: ')
#Prompt user for second item
item2 = input('Enter second item: ')
#Prompt user for third item
item3 = input('Enter third item: ')
#Add items to a list
item_list = [item1, item2, item3]
#Display the list as a single list seperated by commas
print(','.join(item_list))

#Question 3
#Prompt user for sentence
sentence = input('Enter sentence here: ')
#Split sentence 
counter = sentence.split()
#Display the number of words in sentence
print(len(counter))

#Question 4
#Prompt users for input 
five_names = input('Enter 5 names seperated by space: ')
#Convert to lower case
five_names = five_names.lower()
#Split string into list of strings
five_names_list = five_names.split()
#sort list
five_names_sorted = sorted(five_names_list)
#Print names in new lines
for name in five_names_sorted:
    print(name)

#Question 5
#Prompt user for first student's name
student1 = input('Enter first student name: ')
#Prompt user for second student's name
student2 = input('Enter second student name: ')
#Prompt user for third student's name
student3 = input('Enter third student name: ')

#Prompt user for first student's score
score1 = int(input('Enter first Student\'s score here: '))
#Prompt user for second student's score
score2 = int(input('Enter second Student\'s score here: '))
#Prompt user for third student's score
score3 = int(input('Enter third Student\'s score here: '))

#Obtain word length for final formatting
len_1, len_2, len_3 = 45 - len(student1), 45 - len(student2), 45 - len(student3)

#Create title
title = 'Student Score Tracker'

#Print well formatted output
print(f'{title:^45} \n {student1} {score1:>{len_1}} \n {student2} {score2:>{len_2}} \n {student3} {score3:>{len_3}}')

#Question 6
#Prompt user for a word
word = input('Enter word here: ')
#Print length of word
print(len(word))
#Check if word is in upper case
print(f'Upper Case: {word.isupper()}')
#Check if word is in lower case
print(f'Lower Case: {word.islower()}')
#Check if word is in title case
print(f'Title Case: {word.istitle()}')

#Display the reversed word
print(word[::-1])

#Question 7
#Create a list of five cities
five_cities = ['Ibadan', 'Lagos', 'Uyo', 'Sagamu', 'Paris']
#Replace 3rd city with 'London'
five_cities[2] = 'London'
#Display new city list
print(five_cities)
#Remove the last city
five_cities.pop()
#Display new list
print(five_cities)
#Add 'New York' to front of list
new_list = ['New York'] + five_cities
#Display new list
print(new_list)



