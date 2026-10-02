km = float(input('Welcome to Python Exercise 3! Today we are gonna calculate your distance in km, m, cm, mm, and more to get to your destination. So, how many km will you need to get to your destination? '))
hm = km * 10
dam = km * 100
m = km * 1000
dm = km * 10000
cm = km * 100000
mm = km * 1000000
print(f'So you need to go {km} Kilometres right?')
print(f'{km}km will be {hm} Hectometres')
print(f'{dam} Decametres')
print(f'{m} Metres')
print(f'{dm} Decimetres')
print(f'{cm} Centimetres')
print(f'And {mm} Millimetres')
print('Wow thats is a lot of numbers right? lucky us to have those metric units to make things easier')
