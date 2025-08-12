name = 'David' # Define the name variable
age = 78 #Define the age variable
weight = 100.98 #Define the weight variable

print(str, int, float)
# int()
# float()
# str()
# bool()

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
sum_result = num1 + num2
print(f'The sum of {num1} and {num2} is {sum_result}')


#List all the options

print('Welcome, to make enquiries, choose from the options below')
print('1. Airtime and Data rates inquiry')
print('2. Loan rates and maximum loan rates')
print('3. for other services')
print('4. Talk to AI Assistant')

#Get customer's response
response1 = int(input('Choose your preferred enquiry'))

#if 1

print('Welcome, choose from the list below: ')

#List possible options if customer chooses 1

print('Call rates')
print('Data rates')