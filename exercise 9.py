import random
print('Hello again, this time we will pick a random choice, so tell me')
r1 = input('Tell me your 4 favorite things you want to eat today, what is your number 1 choice?')
r2 = input('Thats good, what is your second choice?')
r3 = input('Oh it really looks good too, and now what is your third choice?')
r4 = input('And what is your final choice?')
food = [r1, r2, r3, r4]
today_choice = random.choice (food)
print(f"That's a lot of good foods, and the food you will eat today is:{today_choice}")
