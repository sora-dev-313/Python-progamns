print('Enter 3 numbers:')
a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))

smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

middle = a
if (b > a and b < c) or (b < a and b > c):
    middle = b
if (c > a and c < b) or (c < a and c > b):
    middle = c

print(f'Among these numbers, the highest is {largest}, the middle is {middle}, and the lowest is {smallest}.')
