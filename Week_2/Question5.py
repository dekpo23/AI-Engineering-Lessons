#Task2: Super Market Price List
food_list = ['beans', 'rice', 'yam', 'garri']
food_dic = {}
for food in food_list:
    food_dic[food] = float(input(f'Enter price of {food} here: '))
print(food_dic.keys())
print(food_dic.values())
food = input('Choose food whose price you want to update: ')
new_price = float(input('Enter new price here: '))
food_dic.update({food: new_price})
print(food_dic)