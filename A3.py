""" Use this file to develop and test your Assignment 3 functions. """

import random

def main():
    user_selection = 1
    while user_selection >= 1 and user_selection <= 7:
        print()
        user_selection = get_user_selection()
        print()
        if user_selection == 1:
            print_header(user_selection, "test_get_funny_average()")
            test_get_funny_average()
        elif user_selection == 2:
            print_header(user_selection, "test_get_memory_score()")
            test_get_memory_score()
        elif user_selection == 3:
            print_header(user_selection, "test_get_most_recent()")
            test_get_most_recent()
        elif user_selection == 4:    
            print_header(user_selection, "test_is_legitimate_code()")
            test_is_legitimate_code()
        elif user_selection == 5:    
            print_header(user_selection, "test_get_longest_word()")
            test_get_longest_word()
        elif user_selection == 6:
            print_header(user_selection, "test_remove_triplets()")
            test_remove_triplets()
        elif user_selection == 7:
            print_header(user_selection, "test_get_hand_score()")
            test_get_hand_score()
        print()

def get_user_selection():
    print('   ', 1, ". test_get_funny_average(): ", sep='')
    print('   ', 2, ". test_get_memory_score(): ", sep='')
    print('   ', 3, ". test_get_most_recent(): ", sep='')
    print('   ', 4, ". test_is_legitimate_code(): ", sep='')
    print('   ', 5, ". test_get_longest_word(): ", sep='')
    print('   ', 6, ". test_remove_triplets(): ", sep='')
    print('   ', 7, ". test_get_hand_score(): ", sep='')
    print('   0. Quit: ')
    return int(input("      Enter selection: "))
#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# Score a hand of random dice throws - 2 marks
#--------------------------------------------------
"""
In a dice rolling game a hand is made up of any number of random dice throws and is valued in the following way:

 鈥� In this game a run is a sequence of dice values starting from 1, e.g., 123, 12345, 1234, 1.
 鈥� Each dice which is part of a run of dice starting from a 1 has a value which is equivalent to the dice number. 
   The value of any dice which is part of a run is added to the hand score.
 鈥� If there is no 1 in a hand of dice, the score for the whole hand is 0.
 鈥� A hand of dice can contain more than one run.
	
Study the following five example hands of dice and their corresponding valuation.  Make sure you understand how the hands are valued:

[5, 3, 2, 5, 4, 5, 6, 4, 3] has value 0
[3, 4, 1, 5, 3, 1, 4, 6] has value 2 (contains one run with just the dice [1] and a second run with just [1])
[5, 3, 2, 2, 6, 4, 5, 1, 4] has value 21 (contains one run with the dice [1, 2, 3, 4, 5, 6])
[2, 1, 1, 1, 2, 3, 3, 1, 3, 2] has value 19 (contains three separate runs with the dice [1, 2, 3] 
    and a second run with the dice [1]
[3, 4, 1, 5, 2, 1, 5, 1, 2, 3, 4, 6] has value 37 (contains one run with the dice [1, 2, 3, 4, 5, 6], 
    a second run with [1, 2, 3, 4, 5] and a third run with the dice [1])

Complete the get_hand_score() function which is passed a list of dice throws and returns the value of the hand according to the rules described
above. 
""" 
def get_hand_score(list_of_dice): 
    list_of_dice.sort()
    num = 1
    score = 0
    if 1 not in list_of_dice:
        score = 0
        return score
    while num in list_of_dice:
        if 1 in list_of_dice:
            score += 1
            list_of_dice.pop(list_of_dice.index(1))
            if 2 in list_of_dice:
                score += 2
                list_of_dice.pop(list_of_dice.index(2))
                if 3 in list_of_dice:
                    score += 3
                    list_of_dice.pop(list_of_dice.index(3))
                    if 4 in list_of_dice:
                        score += 4
                        list_of_dice.pop(list_of_dice.index(4))
                        if 5 in list_of_dice:
                            score += 5
                            list_of_dice.pop(list_of_dice.index(5))
                            if 6 in list_of_dice:
                                score += 6
                                list_of_dice.pop(list_of_dice.index(6))
    return score

def test_get_hand_score():
    print("1.  score: ", get_hand_score([5, 3, 2, 5, 4, 5, 6, 4, 3]))
    print("2.  score: ", get_hand_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print("3.  score: ", get_hand_score([5, 3, 2, 2, 6, 4, 5, 1, 4]))
    print("4.  score: ", get_hand_score([2, 1, 1, 1, 2, 3, 3, 1, 3, 2]))
    print("5.  score: ", get_hand_score([3, 4, 1, 5, 2, 1, 5, 1, 2, 3, 4, 6]))


    list1 = [5, 3, 2, 5, 5, 6, 4, 3, 2, 1, 1, 5, 2, 5, 1]
    list1_copy = list1[::]
    list1_copy.sort()
    print("6.  list: ", list1)
    score1 = get_hand_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
    print()

    list1 = [5, 3, 2, 6, 4, 5, 1, 4, 1, 2, 6, 4]
    list1_copy = list1[::]
    list1_copy.sort()
    print("7.  list: ", list1)
    score1 = get_hand_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
    print()

    list1 = [2, 1, 1, 1, 2, 3, 3, 2, 3]
    list1_copy = list1[::]
    list1_copy.sort()
    print("8.  list: ", list1)
    score1 = get_hand_score(list1)
    print("    list_sorted: ", list1_copy)
    print("    score:", score1)
#--------------------------------------------------
#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# Remove triplets made up of three sequential
# identical elements - 3 marks
#--------------------------------------------------
"""
Define the remove_triplets() function which is passed a list of integers as a parameter. The function removes all triplets from the list (i.e.,
removes any three elements in the list which are exactly the same and are in sequence). For example, the following code:

a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
remove_triplets(a_list)
print("1.", a_list)

a_list = [6, 6, 6, 7, 6, 6, 6, 6, 6]
remove_triplets(a_list)
print("2.", a_list)

a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
remove_triplets(a_list)
print("3.", a_list)

a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
remove_triplets(a_list)
print("4.", a_list)

a_list = [1, 1, 2, 1, 2, 2]
remove_triplets(a_list)
print("5.", a_list)

prints:

1. [7, 3]
2. [7, 6, 6]
3. [7, 6, 6, 4, 3]
4. []
5. [1, 1, 2, 1, 2, 2]
"""
def remove_triplets(a_list):
    if len(a_list) < 3:
        pass
    else:
        for index in range(len(a_list) -1, -1, -1):
            if len(a_list) > index + 2:
                if a_list[index] == a_list[index + 1] and a_list[index] == a_list[index + 2]:
                    a_list.pop(index)#pop the first index
                    a_list.pop(index)#pop the second index (index + 1)
                    a_list.pop(index)#pop the third index (index + 2)
    pass

def test_remove_triplets():
    a_list = [6, 6, 6, 7, 6, 6, 6, 3, 3, 3, 8, 8, 8, 3]
    remove_triplets(a_list)
    print("1.", a_list)

    a_list = [6, 6, 6, 7, 6, 6, 6, 6, 6]
    remove_triplets(a_list)
    print("2.", a_list)

    a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
    remove_triplets(a_list)
    print("3.", a_list)

    a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
    remove_triplets(a_list)
    print("4.", a_list)

    a_list = [1, 1, 2, 1, 2, 2]
    remove_triplets(a_list)
    print("5.", a_list)

    list1 = []
    print("6. Before:", list1, end = "     ")
    remove_triplets(list1)
    print("After:", list1)

    list1 = [1, 1, 1, 3, 8, 4, 5, 5, 5]
    print("7. Before:", list1, end = "     ")
    remove_triplets(list1)
    print("After:", list1)
#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# Returns the longest word (which has six or more
# characters) from the parameter list - 3 marks
#--------------------------------------------------
"""
Define the get_longest_word() function which is passed a list of strings as a parameter. The function returns the word in the list which has
the most characters (i.e., the longest word) BUT only words with six or more characters are considered. If two or more words in the list have the
same number of characters as the longest word, the function should return the last word from the start of the list which has the most characters.
If the parameter list is empty or if there are no words in the list with six or more characters, the function should return the empty string. For
example, the following code:

print("1.", get_longest_word(["Melissa", "Jessie", "Kath", "Amity", 
													"Raeann"]))
print("2.", get_longest_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", 
													"Pamelita"]))
print("3.", get_longest_word(["Alan", "Jess", "Amity", "Rosalie",
													"Rosetta"]))
print("4. ", "***", get_longest_word(["Jo", "Jai", "Jen", "Jing", "Joey",
											"Jess"]), "***", sep = "")
print("5. ", "***", get_longest_word([]), "***", sep = "")
print("6.", "***" + get_longest_word([""]) + "***")

prints:

1. Melissa
2. Pamelita
3. Rosetta
4. ******
5. ******
6. ******
"""
def get_longest_word(word_list):
    a_list = list()
    if len(word_list) < 1:
        return ""
    for element in word_list:
        if len(element) >= 6:
            a_list += [element]
    if len(a_list) < 1:
        return ""
    elif len(a_list) == 1:
        return a_list[-1]
    elif len(a_list) > 1:
        for words in range(len(a_list) -1, -1, -1):
            longest_word = a_list[-1]
            if len(a_list[words]) > len(longest_word):
                longest_word = a_list[words]
    return longest_word

"""
def get_longest_word(word_list):
    if len(word_list) == []:
        return ""
    for element in range(len(word_list)-1, -1, -1):
        if len(word_list[element]) < 6:
            word_list.pop(element)
            if len(word_list) == 0:
                return ""
    longest_word = ""
    for words in range(len(word_list) -1, -1, -1):
        if len(word_list[words]) > len(longest_word):
            longest_word = word_list[words]
    return longest_word (杨茗的similar code）- check用的code
"""

def test_get_longest_word():
    print("1.", get_longest_word(["Melissa", "Jessie", "Kath", "Amity", "Raeann"]))
    print("2.", get_longest_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", "Pamelita"]))
    print("3.", get_longest_word(["Alan", "Jess", "Amity", "Rosalie", "Rosetta"]))
    print("4. ", "***", get_longest_word(["Jo", "Jai", "Jen", "Jing", "Joey", "Jess"]), "***", sep = "")
    print("5. ", "***", get_longest_word([]), "***", sep = "")
    print("6.", "***" + get_longest_word([""]) + "***")
#---------------------------------------------
#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# Returns True if the parameter string is a
# legitimate code, the function returns
# False otherwise - 3 marks
#--------------------------------------------------
"""
Define the is_legitimate_code() function which is passed a string as a parameter. The function returns a boolean indicating whether the
parameter string is a legitimate code or not. A legitimate code is a string made up of one letter followed by one or more digits (can also include
spaces before, between or after the digits). The first three lines of code inside the function should be:

  code_letters = ["S", "B", "N", "T", "P"]
  min_for_each_letter = [1, 3, 4, 0, 3] #inclusive
  max_for_each_letter = [7, 9, 6, 7, 5] #inclusive

where:

 鈥ode_letters is the list of code letters which are legitimate for the first letter of the code string,
 鈥in_for_each_letter is a list which contains the minimum number (inclusive) for each digit following that letter, 
 鈥ax_for_each_letter is a list which contains the maximum number (inclusive) for each digit following that letter.

For example, the third element of the code_letters list is the letter 'N', the corresponding third element of the min_for_each_letter list is 4
and the corresponding third element of the max_for_each_letter list is 6. This indicates that the code digits which follow the letter 'N' can be
any number made up of the digits 4, 5 or 6. The number part of a legitimate code string can also contain any number of spaces.

Note: The number part of a parameter code string to be tested could contain an alphabetic character thus making the code not legitimate. You will
find it useful to use the isdigit() method which returns True if a string is a digit, False otherwise.

For example, the following code:

print("1.", is_legitimate_code('B747346'))
print("2.", is_legitimate_code('N  444  454'))
print("3.", is_legitimate_code('T 400 4854'))
print("4.", is_legitimate_code('S  444S454'))
print("5.", is_legitimate_code('P  '))
print("6.", is_legitimate_code('T  0  '))

prints:

1. True
2. True
3. False
4. False
5. False
6. True
"""
def is_legitimate_code(code_str):
    code_letters = ["S", "B", "N", "T", "P"]
    min_for_each_letter = [1, 3, 4, 0, 3] #inclusive
    max_for_each_letter = [7, 9, 6, 7, 5] #inclusive
    if code_str[0] not in code_letters:
        return False
    elif code_str[0] in code_letters:
        code_str = code_str.strip()
        code = code_letters.index(code_str[0])
        minimum = min_for_each_letter[code]
        maximum = max_for_each_letter[code]
        numbers = code_str[1:]
        numbers = numbers.strip()
        if len(numbers) < 1:
            return False
        string = list(numbers)
        result = []
        space = ' '
        if len(string) == 0: 
            return False
        for element in range(len(string) -1, -1, -1):
            if space in string:
                string.pop(string.index(space))
        for index in range(len(string)):
            if string[index].isdigit():
                if int(string[index]) < minimum or int(string[index]) > maximum:
                    result += [False]
                else:
                    result += [True]
            else:
                result += [False]
        if False in result:
            return False
        else:
            return True
        """    if code_str[0] not in code_letters:
        return False
    elif code_str[0] in code_letters:
        code_str = code_str.strip()
        numbers = code_str[1:]
        if len(numbers) < 1:
            return False
        index = code_letters.index(code_str[0])
        maximum = max_for_each_letter[index]
        minimum = min_for_each_letter[index]
        new_list = list(range(minimum, maximum + 1))
        space = " "
        for num in range(len(numbers) -1, -1, -1):
            if numbers[num].isdigit():
                if int(numbers[num]) not in new_list:
                    return False
                else:
                    if numbers[num] != space:
                        return False
        return True (杨茗的code） """
"""
OR
    code_letters = ["S", "B", "N", "T", "P"]
    min_for_each_letter = [1, 3, 4, 0, 3] #inclusive
    max_for_each_letter = [7, 9, 6, 7, 5] #inclusive
    code_str = code_str.strip()
    code = code_letters.index(code_str[0])
    minimum = min_for_each_letter[code]
    maximum = max_for_each_letter[code]
    numbers = code_str[1:]
    numbers = numbers.strip()
    if len(numbers) == 0:
        return False
    for element in range(len(numbers) -1, -1, -1):
        if numbers[element].isdigit():
            if int(numbers[element]) < minimum or int(numbers[element]) > maximum:
                return False
        else:
            if numbers[element] != " ":
                return False
    return True
"""


def test_is_legitimate_code():
    print("1.", is_legitimate_code('B747346'))
    print("2.", is_legitimate_code('N  444  454'))
    print("3.", is_legitimate_code('T 400 4854'))
    print("4.", is_legitimate_code('S  444S454'))
    print("5.", is_legitimate_code('P  '))
    print("6.", is_legitimate_code('T  0  '))

    codes_to_check = ['B45 5', "P-534", 'S5 45 4 4 54', 'B3 9S56 8 ']
    number = 7

    for code in codes_to_check:
        print(str(number) + ". ", code, ":  ", is_legitimate_code(code), sep = "")
        number = number + 1
#--------------------------------------------------
# 3333333333333333333333333333333333333333333333333
# Returns the number from a list of numbers to test
# which is the most recent number in a separate
# list of numbers. - 3 marks
#--------------------------------------------------
"""
Define the get_most_recent() function which is passed two lists of numbers as parameters:  

  鈥� a list of numbers which are in order from the least recent to the most recent, i.e., the number at the end of the list is the most recent,
and
  鈥� a list of numbers to test - the numbers of this list may or may not be elements of the first parameter list.  

This function returns the number from the "list of numbers to test" which occurred most recently in the first parameter list (i.e., is closer to
the end of the list). If none of the numbers in the "numbers to test" list occurred in the first parameter list, the function should return -1.
For example, the following code:

print("1.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [2, 0, 3]))
print("2.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [0, 7, 2]))
print("3.", get_most_recent([0, 1, 2, 8, 9, 0, 3, 4, 6], [1, 9, 2, 8]))
print("4.", get_most_recent([4, 1, 4, 5, 4, 1], [0, 7, 3]))
print("5.", get_most_recent([8, 1, 2, 0, 8, 4, 1], [8, 7, 3]))
print("6.", get_most_recent([], [8, 1, 0, 3]))
numbers_in_order = [1, 1, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0, 3, 4, 1, 2, 4, 
										0, 3, 8, 8, 5, 5]
print("7.", get_most_recent(numbers_in_order, [1, 0, 3, 4] ))
numbers_in_order = [1, 2, 2, 2, 2, 3, 1, 3, 8, 0]
print("8.", get_most_recent(numbers_in_order, [1, 8, 2, 3, 4, 2]))

prints:

1. 3
2. 0
3. 9
4. -1
5. 8
6. -1
7. 3
8. 8
"""
def get_most_recent(numbers_in_order, numbers_to_test):
    for index in range(len(numbers_in_order) - 1, -1, -1):
        for num in numbers_to_test:
            if num == numbers_in_order[index]:
                return num
    if numbers_to_test not in numbers_in_order:
        return -1

def test_get_most_recent():
    print("1.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [2, 0, 3]))
    print("2.", get_most_recent([0, 1, 2, 0, 3, 4, 1], [0, 7, 2]))
    print("3.", get_most_recent([0, 1, 2, 8, 9, 0, 3, 4, 6], [1, 9, 2, 8]))
    print("4.", get_most_recent([4, 1, 4, 5, 4, 1], [0, 7, 3]))
    print("5.", get_most_recent([8, 1, 2, 0, 8, 4, 1], [8, 7, 3]))
    print("6.", get_most_recent([], [8, 1, 0, 3]))
    numbers_in_order = [1, 1, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0, 3, 4, 1, 2, 4, 0, 3, 8, 8, 5, 5]
    print("7.", get_most_recent(numbers_in_order, [1, 0, 3, 4] ))
    numbers_in_order = [1, 2, 2, 2, 2, 3, 1, 3, 8, 0]
    print("8.", get_most_recent(numbers_in_order, [1, 8, 2, 3, 4, 2]))
#--------------------------------------------------
# 2222222222222222222222222222222222222222222222222
# Returns the score from a memory game.
# The strategy is to remove the number that has
# been in the memory the longest time. - 3 marks
#--------------------------------------------------
"""
A memory game is played (and scored) as follows: Random numbers between 0 and 10 (zero inclusive) are called out one at a time. In this memory
game the player can remember a maximum of 5 previously called out numbers. If the called number is already in the player's memory, a point is
added to the player's score. If the called number is not in the player's memory, the player adds the called number to his memory, first removing
another number if his memory is full. In our simulation of this game, the number which is removed from the player's memory is the number that has
been in the player's memory the longest time. For example, if the random numbers are [3, 4, 3, 0, 7, 4, 5, 2, 1, 3], the game proceeds as follows:

Called number 3:  Score: 0, Numbers in memory: [3]
Called number 4:  Score: 0, Numbers in memory: [3, 4]
Called number 3:  Score: 1, Numbers in memory: [3, 4]
Called number 0:  Score: 1, Numbers in memory: [3, 4, 0]
Called number 7:  Score: 1, Numbers in memory: [3, 4, 0, 7]
Called number 4:  Score: 2, Numbers in memory: [3, 4, 0, 7]
Called number 5:  Score: 2, Numbers in memory: [3, 4, 0, 7, 5]
Called number 2:  Score: 2, Numbers in memory: [4, 0, 7, 5, 2]
Called number 1:  Score: 2, Numbers in memory: [0, 7, 5, 2, 1]
Called number 3:  Score: 2, Numbers in memory: [7, 5, 2, 1, 3]

Complete the get_memory_score() function which is passed a list of random numbers as a parameter and returns the final score using the algorithm
described above. For example, the following code:

print("1.  Score:", get_memory_score([3, 4, 1, 6, 3, 3, 9, 0, 0, 0]))
print("2.  Score:", get_memory_score([1, 2, 2, 2, 2, 3, 1, 1, 8, 2]))
print("3.  Score:", get_memory_score([2, 2, 2, 2, 2, 2, 2, 2, 2]))
print("4.  Score:", get_memory_score([1, 2, 3, 4, 5, 6, 7, 8, 9]))
random_nums5 = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 
							4, 8, 3, 0, 3]
print("5.  Score:", get_memory_score(random_nums5))

prints:

1.  Score: 4
2.  Score: 6
3.  Score: 8
4.  Score: 0
5.  Score: 10
"""
def get_memory_score(numbers):
    memory = []
    score = 0
    
    for num in numbers:
        if num not in memory:
            memory += [num]
        else:
            score += 1
        if len(memory) > 5:
            memory.pop(0)
    if score == 0:
        return 0
    else:
        return score

def test_get_memory_score():
    random_nums5 = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
    random_nums6 = [0, 8, 4, 4, 4, 1, 7, 3, 3, 5, 1, 6, 9, 1, 1, 2, 1, 5, 3, 7, 3, 0, 5, 7, 8]
    random_nums7 = [1, 1, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 2, 0, 3, 4, 1, 2, 4, 0, 1, 2, 4, 0, 4, 
    6, 1, 2, 4, 6, 0, 1, 2, 4, 6, 0, 5, 1, 1, 2, 4, 6, 1, 1, 2, 4, 6, 1, 6, 8, 1, 2, 4, 6, 8, 
    1, 1, 2, 4, 6, 8, 1, 7, 10, 1, 4, 6, 8, 10, 1, 2, 4, 6, 8, 10, 1, 8, 2, 1, 2, 6, 8, 10, 
    1, 2, 4, 6, 8, 10, 2, 9, 4, 1, 2, 4, 8, 10, 1, 2, 4, 6, 8, 10, 3, 10, 1, 1, 2, 4, 8, 10, 
    2, 1, 4, 6, 8, 10, 3]
    print("1.  Score:", get_memory_score([3, 4, 1, 6, 3, 3, 9, 0, 0, 0]))
    print("2.  Score:", get_memory_score([1, 2, 2, 2, 2, 3, 1, 1, 8, 2]))
    print("3.  Score:", get_memory_score([2, 2, 2, 2, 2, 2, 2, 2, 2]))
    print("4.  Score:", get_memory_score([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("5.  Score:", get_memory_score(random_nums5))    
    print("6.  Score:", get_memory_score(random_nums6))
    print("7.  Score:", get_memory_score(random_nums7))
#--------------------------------------------------
# 11111111111111111111111111111111111111111111111111
# Returns the average of a list of numbers (excluding
# all zeroes, all negative numbers and excluding the
# minimum and maximum positive numbers) - 3 marks
#--------------------------------------------------
"""
Define the get_funny_average() function which is passed a list of numbers as a parameter and returns the average of some of the numbers in the
parameter list. The function returns the average of the remaining numbers (rounded to 1 decimal place) after all the following have beeen excluded
from the parameter list of numbers (if they exist in the list):

	鈥� all zeroes, 
	鈥� all negative numbers, 
	鈥� the smallest positive number 
and 
	鈥� the largest positive number,

For example, the following code:

print("1.  Funny average: ", get_funny_average([ 3, 2, 0, 25, 1]))
print("2.  Funny average: ", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
print("3.  Funny average: ", get_funny_average([56, 32, 2, 22, 22]))
print("4.  Funny average: ", get_funny_average([-56, -3, 0, -21, 0, 0, 5]))
print("5.  Funny average: ", get_funny_average([56, 3, 2, 0, 251, 1, 41, 22]))
print("6.  Funny average: ", get_funny_average([-56, -3, 2, 0, -251, 1, -41, 0]))
print("7.  Funny average: ", get_funny_average([]))

prints:

1.  Funny average:  2.5
2.  Funny average:  0
3.  Funny average:  25.3
4.  Funny average:  0
5.  Funny average:  24.8
6.  Funny average:  0
7.  Funny average:  0
"""
def get_funny_average(numbers):
    a_list = []
    for num in numbers:
        if num > 0:
            a_list += [num]
    if len(a_list) < 3:
        return 0
    else:
        a_list.pop(a_list.index(min(a_list)))
        a_list.pop(a_list.index(max(a_list)))
        average = round(sum(a_list) / len(a_list), 1)
    return average
    

def test_get_funny_average():
    print("1.  Funny average: ", get_funny_average([ 3, 2, 0, 25, 1]))
    print("2.  Funny average: ", get_funny_average([-6, -32, 2, 0, -51, 1, 0, 0]))
    print("3.  Funny average: ", get_funny_average([56, 32, 2, 22, 22]))
    print("4.  Funny average: ", get_funny_average([-56, -3, 0, -21, 0, 0, 5]))
    print("5.  Funny average: ", get_funny_average([56, 3, 2, 0, 251, 1, 41, 22]))
    print("6.  Funny average: ", get_funny_average([-56, -3, 2, 0, -251, 1, -41, 0]))
    print("7.  Funny average: ", get_funny_average([]))
#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
