def show_magicians(magicians):
    """show_names"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """adding_the_Great"""
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i].title()
    return magicians

magicians = ['alice', 'brian', 'david']
make_great(magicians[:])
show_magicians(magicians)

print(magicians)


def show_magicians(names):
        for name in names:
                print(name.title())
def make_great(names):
        while names:
                modified_names = 'the Great ' + names.pop()
                new_names.append(modified_names)     
        return new_names
new_names = []
names = ['alice', 'flora', 'brian']
new_names = make_great(names)
print(new_names)