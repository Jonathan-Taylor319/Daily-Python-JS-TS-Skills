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

student_grades = {"Jon": 80, "Jeanette": 90, "Emma": 85, "Alex" : 96, "Olivia": 70}

def listed_scores(grades):
    for index, (name, grade) in enumerate(grades.items()):
        print(f"{index + 1}: {name}:{grade}") # had to google and took me a minute to get this figured out :P
        if grade > 70:
            print(f"{name} passed with a {grade}")
        

    

listed_scores(student_grades)


