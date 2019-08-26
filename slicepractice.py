list = ['one', 'two', 'three','four', 'five']
print("The first three items in the list are:")
for item in list[0:3]:
    print(item.title())
print("Three items from the middle of the list are:")
for item in list[1:4]:
    print(item.title())
print("The last three items in the list are:")
for item in list[-3:]:
    print(item.title())