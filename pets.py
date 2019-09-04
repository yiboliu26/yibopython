pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#8.2
def describe_pet(animal_type, pet_name):
    """show_pet_info"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

def describe_pet(pet_name, animal_type = 'dog'):
    """show_pet_info"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = 'willie')
describe_pet('willie')
describe_pet(animal_type = 'hamster', pet_name = 'harry')

def describe_pet(pet_name, animal_type = 'dog'):
    """show_pet_info"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')
describe_pet(pet_name = 'willie')

describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

def describe_pet(animal_type, pet_name):
    """show_pet_info"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('cat', 'notting')

#practice 8.3
def make_shirt(size, pattern):
    """show_shirt_style"""
    print("\nThe shirt is size " + size.title() + " with a " + pattern + " pattern.")
make_shirt('large', 'punk')

def make_shirt(size, pattern = 'I love Python'):
    """show_shirt_style"""
    print("\nThe shirt is size " + size.title() + " with a " + pattern + " pattern.")
make_shirt('large')

def describe_city(city_name, country):
    """show_city_info"""
    print("\n" +city_name.title() + " is in " + country.title() + ".")
describe_city('reykjavik', 'iceland')
describe_city('beijing', 'china')
describe_city('tokyo', 'japan')
describe_city('dallas', 'usa')

