prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' to finish purchasing!"
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        print(age)

prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' to finish purchasing!"
while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        print(age)

x=2 
while x <=3:
    print(x)