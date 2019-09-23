filename = 'guest.txt'
with open(filename, 'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(name.title())


filename = 'guest_book.txt'
print("Enter 'quit' when you are finished.")
while True: 
    name = input("Enter your name: ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")   
            print("Hello " + name.title() + ", welcome! You have been added to guest book.")

filename = 'why_programing.txt'
print("Enter 'quit' when you are finished.")
while True:
    reason = input("Enter why you like programing: ")
    if reason == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + "\n")
            print("Thank you!")