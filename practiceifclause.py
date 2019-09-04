#5.3
alien_color = 'green'
if 'green' in alien_color:
    reward = 5
print("You have been rewarded with "+ str(reward) +"pt! ")
if 'red' in alien_color:
    print("You have not been rewarded. Keep playing!")

#5.4
alien_color = 'green'
if 'green' in alien_color:
    reward = 5
    print("You are rewarded for " + str(reward)+ "pt.")
else:
    rewadred = 10
    print("You are rewareded for " + str(reward) + "pt.")

#5.5
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("You are rewarded for 5 pts.")
elif 'yellow' in alien_colors:
    print("You are rewarded for 10 pts.")
elif 'red' in alien_colors:
    print("You are rewarded for 15 pts.") 

#5.6
age = 12
if age < 2:
    print("You are an infant!")
elif age < 4:
    print("You are learning to walk.")
elif age < 13:
    print("You are still a kid!")
elif age < 20:
    print("You are still an adolescent!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are old!")

#5.7
favorite_fruit = ['banana', 'apple', 'orange']
if 'banana' in favorite_fruit:
    print("You really like bananas!")
if 'apple' in favorite_fruit:
    print("You really like bananas!")