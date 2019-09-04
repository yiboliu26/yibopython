class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()



class Restaurant():
    def __init__(self, restaurant_type, cuisine_type):
        self.rt = restaurant_type
        self.ct = cuisine_type
        self.number_served = 0 
    def describe_restaurant(self):
        print(self.rt.title() + " is easy to remember.")
        print(self.rt.title() + " is very special.")
    def open_restaurant(self):
        print(self.ct.title() + " sounds quite appetite.")
    def serve(self):
        print("This restaurant has served " + str(self.number_served) + " people in the past.")
    def set_number_served(self, numbers):
        self.number_served = numbers
    def increment_number_served(self, people):
        self.number_served += people


my_restaurant = Restaurant('osaka', 'japanese food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 300
my_restaurant.serve()
my_restaurant.set_number_served(1959)
my_restaurant.serve()
my_restaurant.increment_number_served(150)
my_restaurant.serve()




class User():
    def __init__(self, first_name, last_name, ):
        self.first = first_name
        self.last = last_name
        self.login_attempts = 0 
    def describe_user(self):
        print("\nUser information: " + self.first.title() + " " +self.last.title() + ".")
    def greet_user(self):
        print("Howdy, " + self.first.title() + " " +self.last.title() + "!")
    def read_login_attempts(self):
        print("You have attempted to log in for " + str(self.login_attempts) + " times.")
    def check_login_attempts(self, times):
        self.login_attempts = times
    def increment_login_attempts(self, repeating = 1):
        self.login_attempts += 1
    def reset_login_attempts(self, reset=0):
        self.login_attempts = reset


new_user = User('jim', 'green')
new_user.describe_user()
new_user.greet_user()

new_user = User('yibo', 'liu')
new_user.describe_user()
new_user.greet_user()
new_user.login_attempts = 5
new_user.read_login_attempts()
new_user.check_login_attempts(15)
new_user.read_login_attempts()
new_user.increment_login_attempts()
new_user.read_login_attempts()
new_user.reset_login_attempts()
new_user.read_login_attempts()
