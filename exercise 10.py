import random

print("Now let's randomize your household chores!")
h1 = input('Tell me 3 household chores you need to do today in order, and I\'m gonna make an order of which one you should start with. Tell me the first one: ')
h2 = input('Ok, now tell me the next one: ')
h3 = input('Alright, now tell me the last one: ')

ra = [h1, h2, h3]
random.shuffle(ra)

print(f'The household chores order you need to do is: {ra}')
