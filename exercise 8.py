from math import hypot
op = float(input('Welcome! I will help you calculate the hypotenuse. First, tell me the length of the opposite side:'))
ad = float(input('Now, enter the length of the adjacent side: '))
print(f'The length of the hypotenuse is: {hypot(op, ad):.2f}')
