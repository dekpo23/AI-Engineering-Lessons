# Question 1
#Prompt user for message 
message = input('Enter your message here: ')
#Print message in upper case
print(message.upper())






# Question 2
#Create and store string in string variable
string = 'python'
#Print first letter of string
print(string[0])
#Print last letter of string
print(string[-1])





# Question 3
#Prompt user for name
name = input('Enter your name: ')
#Print final message
print(f'Hello {name}!')





# Question 4
#Create and store string in string variable
string = 'david'
#Print length of string
print(string.rindex(string[-1]) + 1)






# Question 5
#Create and store string in string variable
string = "Hello World"
#Replace World with Python
print(string.replace('World', 'Python'))





#Question 6
#Create and store string in string variable
string = 'Python is the best'
#Check if Python in string
print('python' in string.lower())




#Question 7
#Create and store string in string variable
string = 'David'
#Print reversed string
print(''.join(reversed(string)))




#Question 8
#Create and store string with leading and trailing spaces
string = '  David  '
#Print stripped string
print(string.strip())




#Question 9
#Prompt user for sentence
sentence = input('Enter sentence here: ')
#Convert sentence to lower case
sentence =sentence.lower()
#Obtain the count of all vowels
print(sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u'))




#Question 10
#Create and store string in string variable
string = '1234'
#Convert string to int and multiply by 2
print(int(string) * 2)




#Question 11
#Create and store string in string variable
string = 'apple, banana,orange'
#Create a list of strings using split() method 
print(string.split(','))



#Question 12
#Create and store sentence in sentence variable
sentence = input('Enter sentence here: ')
#Print each word in sentence on a new line
print('\n'.join(sentence.split()))



#Question 13
#Create and store string in string variable
string = 'D boy'
#Replace " " with "_"
print(string.replace(' ', '_'))



#Question 14
#Create and store string in string variable
string = 'Banana'
#Count number of times a appeared
print(string.count('a'))



#Qestion 15

#Create and store string in string variable
string = 'https://google.com'
#Check if string starts with "https://"
print(string.startswith('https://'))
