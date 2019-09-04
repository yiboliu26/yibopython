sandwich_orders = ['beef', 'chicken', 'meatballs', 'pastrami', 'tuna']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your " + finished_sandwich + " sandwich!")
    finished_sandwiches.append(finished_sandwich)
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

sandwich_orders = ['beef', 'chicken', 'meatballs', 'pastrami', 'tuna', 'pastrami', 'pastrami']   
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

dream_places = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    dream_place = input("\nWhere would you go? ")
    dream_places[name] = dream_place
    repeat = input("Would you like to let another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---Polling Results---")
for name, dream_place in dream_places.items():
    print(name +" would like to go to " +dream_place.title() + ",")
