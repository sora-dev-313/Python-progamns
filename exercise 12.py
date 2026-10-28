from random import randint
number = randint(0, 5)
print('=' *20)
print('Lets do a quick game, try to guess the number I have in mind, is a number from 0 to 5')
print('=' *20)
player = int(input('What is yours guess?'))
if number == player:
    print('Well done you are lucky today')
else:
    print(f'Wrong, good luck next time my number was {number}')
