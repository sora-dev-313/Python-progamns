print("Let's calculate the cost of a trip")
print('For a short trip each km costs 0.55 and for a long trip it costs 0.45')
km = float(input('Tell me, how many km to your destination? '))
if km <= 200:
    price = km * 0.55
else:
    price = km * 0.45
print(f'Your trip of {km} km will cost a total of {price:.2f}')

    
      
