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