print("Give me two numbers, I will add them together.")
print("Enter 'q' to quit")
while True:
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    else:
        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print("You can't use text as numbers for addition!")   
        else: 
            print(answer) 