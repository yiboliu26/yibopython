#5.8
users = ['david', 'jack', 'marie', 'eric', 'admin']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
#5.9
user = []
if user:
    for user in users:
        print("Hello " +user.title() + ", welcome!")
else:
    print("We need to find some users!")

#5.10

current_users = ['david', 'jack', 'marie', 'eric', 'admin']
new_users = ['jimmy', 'Jack', 'lily', 'jason','calden']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You will need to choose a different user name.")
    else: 
        print("You username is available to use.")

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
for num in numbers:
    if num < 2:
        print(""+str(num) +"st")
    elif num < 3:
        print(""+str(num) + "nd")
    elif num < 4:
        print(""+str(num) + "rd")
    else:
        print(""+str(num) + "th")
