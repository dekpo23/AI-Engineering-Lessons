# my_module/main.py

import first
import second

print('=== Math Functions===')
print('5 + 3 =', first.add(5, 3))
print('10 - 2 =', first.subtract(10,2))
print('6 * 7 =', first.multiply(6, 7))
print('20 / 5 = ', first.divide(20,5))

# Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet('Ridwan'))


