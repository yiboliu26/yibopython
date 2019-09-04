def city_country(city_name, country_name):
    """show_city_info"""
    city = city_name + ', ' + country_name 
    return city.title()
place = city_country('santiago', 'chile')
print(place + "!")
place = city_country('tokyo', 'japan')
print(place + "!")
place = city_country('beijing', 'china')
print(place + "!")
place = city_country('dallas', 'usa')
print(place + "!")

def make_album(singer_name, album_name):
    """singer_and_album_info"""
    person = {'singer': singer_name, 'album': album_name}
    return person
musician = make_album('taylor', '1989')
print(musician)
musician = make_album('drake', 'hotline')
print(musician)
musician = make_album('bieber', 'despacito')
print(musician)

def make_album(singer_name, album_name, number=''):
    """singer_and_album_info"""
    person = {'singer': singer_name, 'album': album_name}
    if number:
        person['number'] = number
        return person
musician = make_album('taylor', '1989', number = 20)
print(musician)
musician = make_album('drake', 'hotline', number = 21)
print(musician)
musician = make_album('bieber', 'despacito', number = 10)
print(musician)

def make_album(singer_name, album_name):
    """album_info"""
    album = singer_name + ' ' + album_name
    return album.title()
while True:
    print("\nnPlease tell me your favorite singer name:")
    print("(Enter 'q' at any time to quit)")
    s_name = input("Singer name: ")
    if s_name == 'q':
        break
    a_name = input("Album name: ")
    if a_name == 'q':
        break
    favorite_album = make_album(s_name, a_name)
    print("\nMy favorite album is " + favorite_album.title() + "!")
