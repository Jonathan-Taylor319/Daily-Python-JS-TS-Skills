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
