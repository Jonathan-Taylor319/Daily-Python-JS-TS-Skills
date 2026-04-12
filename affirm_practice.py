# Problem 1 — Warm Up
# Write a function called count_words that takes a string sentence and returns a dictionary where each key is a word and the value is how many times it appears.

# def count_words(string_sentence):
#     word_count = {}
#     for word in string_sentence.lower().split():
#         word_count[word] = word_count.get(word, 0) + 1
#     return word_count

# print(count_words("this is my string lets try it"))
# print(count_words("My dog is Watching TV with us, i think she is enjoying it"))



# Problem 2
# Write a function called first_non_repeating that takes a string and returns the first character that appears only once. If there's no such character, return "-1" (as a string).

# def first_non_repeating(string):
#     check_for_doubles = {}
#     for letter in string.lower():
#         check_for_doubles[letter] = check_for_doubles.get(letter, 0) + 1
#     for letter, count in check_for_doubles.items():
#         if count == 1:
#             return letter
#     return "-1"
    
# print (first_non_repeating("asadasdaw"))
        
# def most_common_char(string):
#     character_count = {}
#     for letter in string.lower():
#         character_count[letter] = character_count.get(letter, 0) + 1
#     most_common = max(character_count.values())
#     for item, details in character_count.items():
#         if details == most_common:
#             return item
# print(most_common_char("aadsdwdadsw"))
# print(most_common_char("aabbbcc"))   # should be "b"
# print(most_common_char("aabbcc"))    # should be "a"

# Write a function called is_palindrome that takes a string and returns True if it's a palindrome, False if not. Case insensitive.

# def is_palindrome(string):
#     string = string.lower()
#     backwords = string[::-1]
#     return string == backwords

# print(is_palindrome("racecar"))
# print(is_palindrome("race"))
# print(is_palindrome("bob"))

# Write a function called two_sum that takes a list of numbers and a target, and returns the indices of the two numbers that add up to the target.

# def two_sum(number_list, target):
#     for index, num in enumerate(number_list):
#         for index_2, num_2 in enumerate(number_list):
#             if index == index_2:
#                 continue
#             if num + num_2 == target:
#                 return index, index_2
#     return f"No numbers in list equal {target}"
            
# print(two_sum([1, 2, 3, 4, 5, 6, 7, 8], 15))
# print(two_sum([1, 2], 6))
# print(two_sum([4, 5, 6], 8))

# Write a function called fizzbuzz that takes a number n and returns a list of strings from 1 to n where:

# Multiples of 3 → "Fizz"
# Multiples of 5 → "Buzz"
# Multiples of both → "FizzBuzz"
# Everything else → the number as a string

# def fizzbuzz(n):
#     list_of_fizz_buzz = []
#     for count in range(1, n + 1):
#         if count % 15 == 0:
#             list_of_fizz_buzz.append("FizzBuzz")
#         elif count % 5 == 0:
#             list_of_fizz_buzz.append("Buzz")
#         elif count % 3 == 0:
#             list_of_fizz_buzz.append("Fizz")
#         else:
#             list_of_fizz_buzz.append(count)
#     return list_of_fizz_buzz

# print(fizzbuzz(15))
# print(fizzbuzz(1))
# print(fizzbuzz(35))

# Problem — flatten_list
# Write a function that takes a nested list and returns a single flat list.

# def flatten_list(list_of_lists):
#     new_list = []
#     for num in list_of_lists:
#         for num_2 in num:
#             new_list.append(num_2)
#     return new_list
            
# print(flatten_list([[1, 2], [3, 4], [5, 6]]))
# print(flatten_list([[1, [2, 3]], [4, 5]]))

# # Write a function called group_by_first_letter that takes a list of words and 
# # returns a dictionary where each key is a letter and the value is a list of words starting with that letter.

# def group_by_first_letter(list_of_words):
#     groups = {}
#     for word in list_of_words:
#         groups[word[0]] = groups.get(word[0], [])
#         groups[word[0]].append(word)   
#     print(groups)

# (group_by_first_letter(["apple", "banana", "avocado", "blueberry", "cherry"]))
# # Since we made the key word index 0 - it will append only matching words with the same first lettter 
# # We also use groups[word[0]] = word index 0 because we aren't looking to make nested dict but in fact index 0 

# Problem — find_duplicates
# Write a function that takes a list of numbers and returns a list of numbers that appear more than once. Order doesn't matter.

# def find_duplicate(list_of_numbers):
#     # create a dict to hold the count of each letter
#     number_count = {}
#     # need a list to hold our dupes
#     dupes = []
#     # loop through the list
#     for num in list_of_numbers:
#         # count how many of each number
#         number_count[num] = number_count.get(num, 0) + 1
#     # iterate through dict and unpack
#     for key, value in number_count.items():
#         # check to see if more than one
#         if value > 1:
#             # add to our list
#             dupes.append(key)
#     # return our new list
#     return dupes
    

# print(find_duplicate([1, 2, 3, 2, 4, 3, 5]))

# Problem — longest_word
# Write a function that takes a sentence and returns the longest word. If there's a tie, return the first one.

# def longest_word(string):
#     # Split the string into words
#     list_of_words = string.split()
#     # find the longest word and store it
#     longest_word = max(list_of_words, key=len)
#     # return the word
#     return longest_word

# print(longest_word("this is my string"))
# print(longest_word("SuPER crazy amazing gracious this is amazing"))

# Problem — second_largest
# Write a function that takes a list of numbers and returns the second largest number.

# def second_largest(list_of_nums):
#     # get rid of dupes
#     no_dupes = set(list_of_nums)
#     # sort our list
#     sorted_nums = sorted(no_dupes)
#     # check to see if length of list is over 2
#     if len(sorted_nums) > 1:
#         # return our 2nd highest 
#         return sorted_nums[-2]
#     else:
#         # return none
#         return "None"

# print(second_largest([1, 2, 4, 5, 6, 10, 23, 45, 33]))
# print(second_largest([1, 1, 1]))

# Warm up — is_anagram
# Write a function that takes two strings and returns True if they are anagrams of each other, False if not. Case insensitive.

# def is_anagram(str1, str2):
#     # need to sort and lower the input
#     sorted_and_low = sorted(str1.lower())
#     sorted_and_low_2 = sorted(str2.lower())
#     # compare and check
#     return sorted_and_low == sorted_and_low_2

# print(is_anagram("listen", "silent"))
# print(is_anagram("ascb", "dd"))
    
# Problem — valid_parentheses
# Write a function that takes a string of parentheses and returns True if they are valid (properly opened and closed), False if not.

def valid_parentheses(string):
    # Something to hold our check
    stack = []
    # loop through the string
    for symbol in string:
        # check for opening
        if symbol == "(":
            # if there is the opening add to our check list
            stack.append(symbol)
        # if the symbol closes
        elif symbol == ")":
            # check if list is empty -
            if len(stack) == 0:
                # return false  
                return False
            # else pop out the opening we saved -
            else:
                stack.pop()
    # if check list is empty then we know it opened and closed enough to clear out
    return len(stack) == 0
    
print(valid_parentheses("((()))"))
print(valid_parentheses("(())))"))
print(valid_parentheses(")))"))
print(valid_parentheses("((()))"))