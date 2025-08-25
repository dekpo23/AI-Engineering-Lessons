#Question 1

fruits = input('Enter 5 fruits seperated by space: ')
fruits_set = set(fruits.split())
print(fruits_set)

#Question 2

event_attendance = input('Enter names of people seperated by space here: ')
event_set = set(event_attendance.split())
print(sorted(event_set, key = lambda x:x.lower()))

#Question 3

numbers = set([i for i in range(1, 51)])
num = int(input('Choose the seat number you prefer: '))
numbers.remove(num)
print(numbers)

#Question 4
names = {"David", "Grace", "Mercy"}
your_name = input('Enter your name here: ')
if your_name in names:
    print('Don\'t register twice')
names.add(your_name)
