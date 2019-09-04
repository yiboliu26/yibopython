#7.4
prompt = "\nTell us what toppings you need, we will add for you!"
prompt += "\nEnter 'quit' to finish ordering! "
message = ""
while message != 'quit':
    message = input(prompt)
    print("" +message + " added!")


prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' to finish purchasing!"
age = ""
while age != 'quit':
    age = int(input(prompt))
    if age < 3:
        print("Free!")
    elif age <= 12:
        print("$10")
    else:
        print("$15")



    
    