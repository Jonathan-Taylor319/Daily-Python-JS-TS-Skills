# Python Slicing 

# Core idea:
# Slicing lets you grab part of a sequence like a string, list or tuple

# basic patter:
# thing[start:stop:step]

# meaning:
#     start = where to begin
#     stop = where to end, but not include
#     step = how to move through it

# word = "python"
# print(word[0:3])

# output = pyt

# why? 
#     starts at 0
#     stops before index 3

# word = "python"

# print(word[0:6]) # "python" 0-1-2-3-4-5
# print(word[0:3]) #  "pyt" 0-1-2
# print(word[2:6]) # "thon" 2-3-4-5
# print(word[:3]) # "pyt" 0-1-2
# print(word[2:]) # "thon" 2-3-4-5
# print(word[:]) # "python" start at beginning, stop at end step by 1 (default)

# # Negative Indexing 

# print(word[-1]) # 'n' 5 last item
# print(word[-2]) # 'o' 4 second to last
# print(word[-4:-1]) # 'tho' start at index -4 "t" stop before index -1 "n"
# print(word[::1]) # "python" step by 1t
# print(word[::2]) # "pto" step by 2
# print(word[1::2]) # "yhn" start at index 1 and step by 2
# print(word[::-1]) # "nohtyp" step backwards 

# Negative indexing - Python counts from the end of the sequence instead of the front

# word = "python"

# normal index
# p y t h o n
# 0 1 2 3 4 5

# negative index
#  p  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# what I need to learn
# -1 = last item
# -2 = second - to - last
# -3 = third - to - last

# -number = that index from last don't start at 0 ..... 

# word = "Jonathan"

# print(word[0:4]) # "Jona" right
# print(word[2:6]) # "nath" right
# print(word[:5]) # "Jonat" right
# print(word[-3:]) # "nah" wrong - right letters wrong way :P it's "han"
# print(word[:-2]) # "Jonath" right - start at 0 but stop at 2 from end

# Slicing -
#     a way to extract part of a sequence
#     a way to copy part of data
#     a way to reorder data
#     a way to inspect a section of a string or list

# it supports patterns more than it is the pattern

# 🐍 Challenge 1 — Student Grade Tracker
# Write a Python program that does the following:
# 1. Create a dictionary with at least 4 students and their grades (as numbers):
# e.g. {"Alice": 92, "Bob": 78, ...}
# 2. Print each student's name and grade using a loop — use enumerate so the output looks like:
# 1. Alice — 92
# 2. Bob — 78
# ...
# 3. Find and print the highest grade and which student got it.
# 4. Print only the students who passed (grade >= 70). Use a loop or list comprehension — your call.

# Rules:

# Write it yourself — no AI, no copy-paste
# It doesn't have to be perfect, just try
# If you get stuck, describe where you got stuck and I'll give a hint (not the answer)

# Hints you already know you'll need:

# To get a value from a dict: my_dict["key"] or my_dict.get("key")
# To loop over a dict: for name, grade in my_dict.items()
# enumerate goes on the outside: for i, thing in enumerate(something)

# Take your time, paste your code when you're ready, and don't stress about it being messy. Let's see what you've got! 💪

# student_grades = {"Jon": 80, "Jeanette": 90, "Emma": 85, "Alex" : 96, "Olivia": 70}

# def listed_scores(grades):
#     passed = []
#     failed = []

#     for index, (name, grade) in enumerate(grades.items()):
#         print(f"{index + 1}: {name}: {grade}")
#         if grade > 70:
#             passed.append(name)
#         else:
#             failed.append(name)

#     print("\nPassed:")
#     for name in passed:
#         print(name)

#     print("\nFailed:")
#     for name in failed:
#         print(name)

#     top_student = max(grades, key=grades.get)
#     top_score = grades[top_student]
#     print(f"\nHighest score: {top_student} with a {top_score}")
        
# listed_scores(student_grades)


# 🐍 Challenge 2 — Word Analyzer
# Write a function called analyze_text that takes a string of text as input and does the following:
# 1. Count how many words are in the string
# 2. Print each word with its index using enumerate, starting at 1:
# 1. the
# 2. quick
# 3. brown
# ...
# 3. Print the longest word in the string
# 4. Print all words that are longer than 4 characters
# 5. Print the original sentence but with every word reversed
# "hello world" → "olleh dlrow"

# Test it with this string:
# pythontext = "the quick brown  fox jumps over the lazy dog"

# def analyze_text(text_str):
#     # Got stuck on how to split up the str at first
#     split_str = text_str.split()
#     print(f"There are", len(split_str), "words in this string")

#     words_over_four = []

#     for index, word in enumerate(split_str):
#         print(f"{index + 1}: {word} ")
#         if len(word) > 4:
#             words_over_four.append(word)
    
#     longest_word = max(split_str, key=len)
#     print(f'the longest word is {longest_word}')
    
#     if len(words_over_four) > 0:
#         print("the string has these words over 4:", words_over_four)
#     else:
#         print("there are no words over 4 letters in this string")

#     for index, word in enumerate(split_str):
#         if index % 2 == 0 :
#             print(word[::-1])
#         else:
#             print(word)

    
# analyze_text(pythontext)