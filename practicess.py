number = input("Enter a number, and I'll tell you if it is a 10 folds. ")
number = int(number)
if number % 10 == 0:
    print("Yes, it is!")
else:
    print("No, it is not!")