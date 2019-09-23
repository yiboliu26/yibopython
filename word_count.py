def count_word(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filename = 'alice.txt'
count_word(filename)

filenames = ['alice.txt', 'siddharta.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_word(filename)