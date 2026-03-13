# 3/9/26 
#collections.counter

# problem - find the most common character in a string using Collections.counter

# from collections import Counter

# string1 = 'this is my string'
# string2 = 'this is going to be a longish kind of string to test things'

# def find_most_used(text):
#     counts = Counter(text.replace(" ",""))
#     print(counts.most_common(1))

# find_most_used(string1)
# find_most_used(string2)

# 3/10/26
#set()

# #ex:
# nums = [1,2,2,3,4,4,5]
# nums2 = [1,2,3,4,5,6,7,8,9]
# nums3 = [2, 5, 2, 1, 6, 7, 8, 9, 25, 16]

# # unique_nums = set(nums)
# # print(unique_nums)

# # # membership checking is fast
# # print(3 in nums)

# # names = ['jon', 'john', 'james', 'jon', 'joseph', 'jon']
# # names_of_user_no_duplicates = set(names)
# # print(names_of_user_no_duplicates)
# # print("jon" in names_of_user_no_duplicates)
# # print('sam' in names_of_user_no_duplicates)

# # Given a list of numbers return true if a number appears more than once - 
# # def contains_duplicates(numbers):
# #     nums_duplicates_removed = set(numbers)
# #     return len(numbers) != len(nums_duplicates_removed)

# #same as above but refractured 
# def contains_duplicates(numbers):
#     return len(numbers) != len(set(numbers))

# print(contains_duplicates(nums))
# print(contains_duplicates(nums2))
# print(contains_duplicates(nums3))

# 3/11/26
# Dictionary

# word = "banana"
# counts = {}

# for letter in word:
#     if letter in counts:
#         counts[letter] += 1
#     else:
#         counts[letter] = 1
# print(counts) 

# for letter in word:
#     counts[letter] = counts.get(letter, 0) + 1
# print(counts)

# return the most frequent number in a list
# ages = [21, 44, 31, 21, 45, 50, 21, 40, 44]

# def most_common_age(numbers):
#     age_counter = {}
#     for age in numbers:
#         if age in age_counter:
#             age_counter[age] += 1
#         else:
#             age_counter[age] = 1
#     return max(age_counter, key=age_counter.get)

# # def most_common_age(numbers):
# #     age_counter = {}
# #     for age in numbers:
# #         age_counter[age] = age_counter.get(age, 0) + 1
# #     most_common = max(age_counter, key=age_counter.get) 
# #     return most_common

# print(most_common_age(ages))

# need to write down get() and then max(age_counter, key=age_counter.get) to understand - knew about the get to populate dict but didn't know about for loop to populate

# 3/12/26
# enumerate()

# fruits = ["apple", "banana", "orange"]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# users = ["trix", "jon", "sparky", "cash", "trix"]
# for index, name in enumerate(users):
#     print(index, name)

# numbers = [12, 14, 13, 44, 21, 45, 67, 69]

# def wheres_the_first_even_number(things):
#     things.sort()
#     for index, number in enumerate(things):
#         if (number % 2 == 0):
#             return number
        
# print(wheres_the_first_even_number(numbers))

# 3/13/26
# set()

nums = [1, 2, 2, 3, 4, 4]

unique = set(nums)
print(unique)