#8.1
def greet_user():
    """simple greetings"""
    print("Hello!")
greet_user()

def greet_user(username):
    """simple_greeting"""
    print("Hello, " + username.title()+"!")
greet_user('jessie')
greet_user('sarah')

def display_message(section):
    """knowledge in this chapter"""
    print("We learned " + section.title() + " in this chapter.")
display_message('function')    

def favorite_book(title):
    """favorite_books"""
    print("One of my favorite books is " + title.title() + ".")
favorite_book('alice in wonderland')

def get_formatted_name(first_name, last_name):
    """return_with_neat_names"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#this is an infinite cycle(not)
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
