import random
print ('='*20)
print ('Game')
print ('='*20)
print ('Welcome! Lets play a game of even or odd. You choose first.')
choice = input('Which one do you choose, even or odd?').lower().strip()

if choice == 'even' or choice == 'odd':
    
    if choice == 'even':
        print ('Good your choice is even so I ill go with odd')
    else:
        print ('Good your choice is odd so I ill go with even')

    num = int(input('Ok now chose a number betewm 0 and 5: '))
    nu = random.randint(0, 5)
    print(f'Good your number was {num} now is my turn and my number is {nu}')
    
    som = num + nu
    print (f'The total is {som}')

    if som % 2 == 0:
        result = 'even'
        print('The result is EVEN!')
    else:
        result = 'odd'
        print('The result is ODD!')

    if choice == result:
        print('CONGRATULATIONS YOU WIN!!!')
    else:
        print('Too bad I win')

else:
    print ('Wrong! You need to chose even or odd. Restart the game.')
