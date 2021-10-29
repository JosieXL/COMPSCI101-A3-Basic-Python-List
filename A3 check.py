word_list = ["Jo", "Jessie", "Penelope", "Jin", "Raeann", "Pamelita"]
a_list = list()
if len(word_list) < 1:
    print(" ")
for index in range(len(word_list) -1, -1, -1):
    if len(word_list[index]) >= 6:
        a_list += [word_list[index]]
if len(a_list) < 1:
    print(" ")
elif len(a_list) == 1:
    print(a_list[-1])
elif len(a_list) > 1:
    for words in range(len(a_list) -1, -1, -1):
        longest_word = a_list[-1]
        if len(a_list[words]) > len(longest_word):
            longest_word = a_list[words]
            print(longest_word)

