import json

favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
    print("I know your favorite number! It is " + favorite_number + "!")


import json
filename = 'favorite_number.json'
with open(filename) as f_obj:
    favorite_number = json.load(f_obj)
    print("We know it is " + str(favorite_number) + "!")
