def print_models(unprinted_designs, completed_models):
    """print_and_move"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " +current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


def show_magicians(names):
    """show_names"""
    for name in names:
        print(name.title())

magicians = ['alice', 'brian', 'david']
show_magicians(magicians)


def show_magician(magicians):
    """show_names"""
    for name in magicians:
        print(name.title())


def make_great(magicians):
    """adding_the_Great"""
    for modified_names in range(len(magicians)):
        magicians[modified_names] = 'the Great' + magicians[modified_names]
        return magicians

magicians = ['alice', 'brian', 'david']
show_magicians(magicians)
make_great(magicians)





