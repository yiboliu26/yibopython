car = input("What kind of car would you like to rent? ")
print("Let me see if I can find you a " + car + ".")

people = input("How many of you? ")
people = int(people)
if people >= 9:
    print("We are full right now.")
else:
    print("We have table available!")

