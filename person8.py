def build_person(first_name, last_name):
    """return_to_dictionary_with_personal_info"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """return_to_dict_with_person_info"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
