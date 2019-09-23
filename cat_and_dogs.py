def read_file(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        pass

line = "Row, row, row your boat."
line.count('row')
print(str(line.count('row')))


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_file(filename)

def count(filename):
    try: 
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        print("DNE!")
    else:
        words = contents.split()
        num_words = len(words)
        print("The book " + filename + " has about " + str(num_words) + " words.")

filename = 'sherlock_homes.txt'
count(filename)



