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

class IceCreamStand(Restaurant):
    def __init__(self, resaurant_type, cuisine_type):
        super().__init__(resaurant_type, cuisine_type)
        self.flavors = ['orange', 'mango', 'coconut']
    def describe_flavors(self):
        for flavors in self.flavors:
            print("This restaurant " + self.rt.title() + " of "+ self.ct + " type provides a " + flavors + " taste icecream!")

my_restaurant = IceCreamStand('brawns', 'texas')
my_restaurant.describe_flavors()


from dog import User, Admin
admin_01 = Admin('yibo', 'liu')
admin_01.show_privillages()


