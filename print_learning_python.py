filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

message = "I really like dogs."
message.replace('dog', 'cat')
print(message)


filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.rstrip()
    print(line.replace('python', 'c'))