def get_formatted_name(first_name, last_name):
    """return_neat_names"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """return_formatted_names"""
    full_name = first_name + ' ' +middle_name + ' ' +last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """return_formatted_names"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' +last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)