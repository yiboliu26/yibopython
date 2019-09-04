favorite_languages = {
    'jen': 'python', 
    'sarah': 'C', 
    'edward': 'ruby', 
    'phil': 'python'
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title()+
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " +
    language.title() + ".")


for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

favorite_languages = {
    'jen': 'python', 
    'sarah': 'C', 
    'edward': 'ruby', 
    'phil': 'python'
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + ".")

favorite_languages = {
    'jen': 'python', 
    'sarah': 'C', 
    'edward': 'ruby', 
    'phil': 'python'
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#6.33
favorite_languages = {
    'jen': 'python', 
    'sarah': 'C', 
    'edward': 'ruby', 
    'phil': 'python'
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", Thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())    

candidates = ['jack', 'jason', 'rose', 'sarah', 'luis']
for candidate in favorite_languages.keys():
    if candidate in candidates:
        print("Thank you, " + candidate.title() + "!")
    else:
        print("Hi " + candidate.title() + ", please coordinate with the test!")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t " + language.title())