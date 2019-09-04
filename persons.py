person = {'first_name': 'yibo', 'last_name': 'liu', 'age': 33, 'city': 'dallas'}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

favorite_number = {'flora': 8, 'yibo': 6, 'jack': 1, 'marie': 3, 'rose': 2}
print("Flora's favorite number is " +
    str(favorite_number['flora']) +
    ".")
print("Yibo's favorite number is " +
    str(favorite_number['yibo']) +
    ".")
print("Jack's favorite number is " +
    str(favorite_number['jack']) +
    ".")
print("Marie's favorite number is " +
    str(favorite_number['marie']) +
    ".")
print("Rose's favorite number is " +
    str(favorite_number['rose'])+
    ".")

terms = {
    'dictionary': 'vercabulary', 
    'condition': 'request',
    'tuple': 'list', 
    'slice': 'piece', 
    'clause': 'sentence'
    }
print(terms['dictionary'])
print("Dictionary")
print(terms['dictionary'])
for term, meaning in terms.items():
    print(term.title() + ", means " + meaning+ ".")

terms['for'] = 'cycle'
terms['sort'] = 'arrange'
terms['cd'] = 'change directory'

for term, meaning in terms.items():
    print(term.title() + ", means " +meaning + ". ")

rivers = {'nile': 'egypt', 'chang': 'china', 'mississippi': 'usa'}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

#practice6.7
person_0 = {'first_name': 'yibo', 'last_name': 'liu', 'age': 33, 'city': 'dallas'}
person_1 = {'first_name': 'flora', 'last_name': 'hua', 'age': 30, 'city': 'dallas'}
person_2 = {'first_name': 'andy', 'last_name': 'liu', 'age': 2, 'city': 'dallas'}
people = [person_0, person_1, person_2]
print(people)

#6.8
notting = {'type': 'cat', 'owner': 'yibo'}
elsa = {'type': 'dog', 'owner': 'violin'}
jojo = {'type': 'lab', 'owner': 'jay'}
pets = [notting, elsa, jojo]
print(pets)

#6.9
favorite_places = {
    'yibo': ['beijing', 'shanghai'],
    'flora': ['la', 'nyc'],
    'andy' : ['dallas', 'houston'],
    }
print(favorite_places)
for name, cities in favorite_places.items():
    print(""+ name.title() + "'s favorite cities are:") 
    for city in cities:
        print("\t" +city.title())

favorite_numbers = {
    'flora': [8, 9, 10],
    'yibo': [6, 7, 8],
    'jack': [1, 2, 3], 
    'marie': [3], 
    'rose': [2],
    }
for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t"+str(number))

cities = {
    'beijing':  {
        'country': 'china',
        'population': 1000000,
        'fact': 'rich'
        },
    'dallas': {
        'country': 'usa',
        'population': 2000,
        'fact': 'hot'
        },
    'tokyo': {
        'country': 'japan',
        'population': 30000,
        'fact': 'good',
        },
    }
for city, info in  cities.items():
    print("\nCity name: "+ city.title())
    location = info['country']
    people = info['population']
    condition = info['fact']

    print("\t"+location.title())
    print("\t"+condition.title())
