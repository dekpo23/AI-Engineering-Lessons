for i in range(1,6):
    for j in range(1, i+1):
        print(j, end = '\t')
    print()

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonnaci(n-2) + fibonnaci(n-1)
    
print(fibonnaci(6))

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    for letter in string_:
        if letter in vowels:
            string_ = string_.replace(letter, '')
    return string_

print(disemvowel('David'))
print('Lower'.lower())

dic = {'1': 'good', '2': 'bad'}
print(list(dic.keys()))

print(list(dic.keys()).remove('1'))

rem_dic = 