vel = float(input('Welcome to the radar. The speed limit on this highway is 80 km/h, and exceeding it will result in a fine. Tell me, how fast is the car going?'))
fin = (vel - 80)*7
if vel > 80:
    print(f'You are going too fast and have received a fine of {fin}. Please be more careful and slow down!')
else:
    print('You are driving within the speed limit. Keep it up and have a safe trip!')
