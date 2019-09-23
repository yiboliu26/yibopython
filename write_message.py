filename = 'programing.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

filename = 'programing.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programing.\n")
    file_object.write("I love creating new games.\n")

filename = 'programing.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a brower.\n")