try:
    print(5/0)
except ZeroDivisionError:
    print("You can't dived by zero!")

print("give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    else:
        try:
            answer = int(first_number)/int(second_number)
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            print(answer)
   