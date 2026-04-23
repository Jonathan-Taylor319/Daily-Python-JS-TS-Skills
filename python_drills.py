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

# student_test_grades = {"Jon": 80, "Jeanette": 90, "Emma": 85, "Alex" : 96, "Olivia": 70}

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
        
# listed_scores(student_test_grades)


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
#     print("There are", len(split_str), "words in this string")

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

# movies = {
#     "Inception": {"genre": "sci-fi", "rating": 9.2, "year": 2010},
#     "The Notebook": {"genre": "romance", "rating": 7.8, "year": 2004},
#     "The Dark Knight": {"genre": "action", "rating": 9.5, "year": 2008},
#     "Interstellar": {"genre": "sci-fi", "rating": 8.6, "year": 2014},
#     "Titanic": {"genre": "romance", "rating": 7.9, "year": 1997},
# }
# # ```

# # Write a function called `movie_search` that:

# # **1.** Prints every movie with its rating and year like:
# # ```
# # Inception — 9.2 — 2010

# # 2. Finds and prints the highest rated movie
# # 3. Using a list comprehension, prints all sci-fi movies only
# # 4. Using a list comprehension, prints all movies rated above 8.5

# def movie_search(movie_dict):
#     for movie, movie_details in movie_dict.items():
#         print(movie, movie_details["rating"], movie_details["year"])

#     sci_fi_movies = [movie for movie, movie_details in movie_dict.items() if movie_details["genre"] == "sci-fi"]
        
#     movies_over_eight_five = [movie for movie, movie_details in movie_dict.items() if movie_details["rating"] > 8.5]   
    
#     highest_rated_movie = max(movie_dict, key=lambda movie: movie_dict[movie]["rating"])
#     print("the highest rated movie is", highest_rated_movie)
    
#     print("the sci-fi movies in the list are:", sci_fi_movies)
#     print("these movies have over a 8.5 rating", movies_over_eight_five)

# movie_search(movies)

# 🐍 Challenge 4 — Contact Book
# Build a simple contact book using a dictionary. Write these four functions:
# 1. add_contact(contacts, name, phone, email) — adds a new contact
# 2. remove_contact(contacts, name) — removes a contact, prints a message if name not found
# 3. search_contact(contacts, name) — prints that contact's details, prints a message if not found
# 4. list_all(contacts) — prints all contacts neatly with enumerate
# Test it by calling all four functions with real data.

# contacts = {}

# def add_contact(name, phone, email):
#     contacts[name] = {"phone":phone, "email":email}
#     return contacts

# add_contact("Jon","732-927-0850","email.email.com")
# add_contact("Bob","732-927-9999","lost.email.com")
# add_contact("RON","732-967-0850","apple.email.com")
# add_contact("Bluey","315-927-0850","blue.email.com")
# add_contact("costa","555-555-5555","done.email.com")

# def remove_contact(contacts, name):
#     if name in contacts:
#         del contacts[name]
#     else:
#         print("Name not found")

# remove_contact(contacts, "RON")
# print(contacts)

# def search_contact(contacts, name):
#     if name in contacts:
#         print(f"{name} - {contacts[name]["phone"]} - {contacts[name]["email"]}")
#     else:
#         print("Name not found")

# search_contact(contacts, "Jon")

# def list_all(contacts):
#     for index, name  in enumerate(contacts):
#         print(f"{index + 1}: {name}")

# list_all(contacts)


# 🐍 Challenge 5 — Student Report Card
# Build a student grade tracker that feels like a real tool. You'll need these functions:
# 1. add_student(students, name, grades) — adds a student with a list of grades
# pythonadd_student(students, "Jon", [85, 92, 78, 95, 88])
# 2. get_average(students, name) — calculates and prints a student's average grade
# 3. get_letter_grade(average) — returns a letter grade based on the average:

# 90+ = "A"
# 80+ = "B"
# 70+ = "C"
# below 70 = "F"

# 4. print_report(students) — prints every student, their average, and their letter grade using enumerate
# Test with at least 4 students each with 5 grades.

# student_test_grades = {}
# student_quiz_grades = {}

# def add_student(student_test_grades, name, grades):
#     student_test_grades[name] = {"grades":grades}
#     return student_test_grades

# add_student(student_test_grades, "Jonathan", [90, 85, 86, 99, 94])
# add_student(student_test_grades, "Bob", [65, 75, 70, 90, 40, ])
# add_student(student_test_grades, "George", [80, 85, 87, 80, 83])
# add_student(student_test_grades, "Richard", [70, 99, 80, 75, 95])
# add_student(student_test_grades, "Doug", [99, 100, 95, 98, 0])

# add_student(student_quiz_grades, "jonathan", [100, 100, 98, 99, 100])
# add_student(student_quiz_grades, "Bob", [88, 67, 98, 76, 44])
# add_student(student_quiz_grades, "George", [90, 80, 70, 60, 100])
# add_student(student_quiz_grades, "Richard", [70, 99, 80, 75, 95])
# add_student(student_quiz_grades, "Doug", [60, 67, 68, 65, 90])

# def print_list_of_students_grades_simple(student_grades, label):
#     print(f"\n{label}")
#     for student, details in student_grades.items():
#         print(student, details)

# print_list_of_students_grades_simple(student_test_grades, "Test Scores")
# print_list_of_students_grades_simple(student_quiz_grades, "Quiz Scores")

# def get_average(student_grade_dict, name):
#     if name in student_grade_dict:
#         grades = student_grade_dict[name]["grades"]
#         average_grade = sum(grades)/len(grades)
#         return average_grade
#     else:
#         print(f"{name} not found")
        
# print(get_average(student_test_grades, "Jonathan"))

# def get_letter_grade(average):
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     else:
#         return "F"

# def print_report(students):
#     for index, student in enumerate(students):
#         print(f"{index + 1}. {student}",get_letter_grade(get_average(students, student)))
    

# print_report(student_test_grades)
# print_report(student_quiz_grades)
    
# 🐍 Challenge 6 — Library Book Tracker
# Build a library system with these functions:
# 1. add_book(library, title, author, pages) — adds a book
# 2. check_out(library, title) — marks a book as checked out, prints error if not found or already checked out
# 3. return_book(library, title) — marks a book as returned, prints error if not found or not checked out
# 4. available_books(library) — prints only books that are NOT checked out
# 5. longest_book(library) — prints the book with the most pages

# library_book_inventory = {}

# def add_book(inventory, title, author, pages, checkout_status):
#     inventory[title] = {"Author": author, "pages": pages, "Check_out Status": checkout_status }
#     return inventory

# add_book(library_book_inventory, "James and the Giant Peach", "Some Author", 245, False)
# # print(library_book_inventory)

# add_book(library_book_inventory, "The Quest", "Jean Clead VanDamn", 600, False)
# add_book(library_book_inventory, "The Odessy", "Some good Author", 900, False)
# add_book(library_book_inventory, "Romeo and Juliet", "Shakesdude", 1050, False)
# add_book(library_book_inventory, "Live Laugh Love", "Some Chick",  2500, False)
# add_book(library_book_inventory, "The Client", "John Grisham", 3000, False)
# add_book(library_book_inventory, "How to Stop Smoking", "John C Smith", 250, False)

# def simple_inventory_check(inventory):
#     for book in inventory.items():
#         print(book)

# def check_out_book(inventory, title):
#     if title in inventory:
#         checkout_status = inventory[title]["Check_out Status"]
#         if title in inventory and checkout_status == True:
#             print("Sorry book checked out")
#         elif title in inventory and checkout_status == False:
#             inventory[title]["Check_out Status"] = True
#             print(f"{title}, is now checked out. please bring back in two weeks")
#     else:
#         print(f"{title} not found at this library")

# check_out_book(library_book_inventory, "The Quest")
# check_out_book(library_book_inventory, "Hunger Games")

# def return_book(inventory, title):
#     if title in inventory:
#         checkout_status = inventory[title]["Check_out Status"]
#         if title in inventory and checkout_status == False:
#             print("Sorry - you cant check in a book thats not checked out")
#         elif title in inventory and checkout_status == True:
#             inventory[title]["Check_out Status"] = False
#             print(f"Thanks for returning: {title}")
#     else:
#         print(f"{title} does not belong at this library")

# return_book(library_book_inventory, "The Quest")

# def available_books(inventory):
#     for title in inventory:
#         if inventory[title]["Check_out Status"] == False:
#             print(f"{title} is available to be checked out")

# def longest_book(inventory):
#     return max(inventory, key=lambda title:inventory[title]["pages"])
    
# check_out_book(library_book_inventory, "How to Stop Smoking")      
# check_out_book(library_book_inventory, "Romeo and Juliet")      
# available_books(library_book_inventory)
# print(longest_book(library_book_inventory), "is the longest book")

# 🐍 Challenge 7 — Safe Calculator
# Write a calculator function called calculate(num1, num2, operation) that supports these operations: "add", "subtract", "multiply", "divide".
# Requirements:
# 1. Handle the operation using if/elif/else
# 2. Use try/except to handle two specific errors:

# Dividing by zero
# Someone passing in a string instead of a number

# 3. Return the result, or a helpful error message

# def calculate(num1, num2, operation):
#     try:
#         if operation == "add":
#             return num1 + num2
#         elif operation == "subtract":
#             return num1 - num2
#         elif operation == "multiply":
#             return num1 * num2
#         elif operation == "divide":
#             try:
#                 return num1 / num2
#             except ZeroDivisionError:
#                 if num1 or num2 == 0:
#                     return "divide by zero"
#         else:
#             return "unknown operation"
#     except TypeError:
#         return "invalid input"

# print(calculate(10, 2, "divide"))    # normal
# print(calculate(10, 0, "divide"))    # divide by zero
# print(calculate(10, "cat", "add"))    # invalid input
# print(calculate(10, 2, "multiply"))   # normal
# print(calculate(10, 2, "blah"))     # unknown operation


# 🐍 Challenge 8 — Expense Tracker
# Build a personal expense tracker with these functions:
# 1. add_expense(expenses, category, amount, description) — adds an expense
# pythonadd_expense(expenses, "food", 12.50, "Chipotle")
# 2. total_spent(expenses) — returns total amount spent across all expenses
# 3. spent_by_category(expenses) — returns a dict showing total spent per category
# 4. most_expensive(expenses) — returns the single most expensive expense
# 5. expenses_over(expenses, amount) — returns a list of all

# total_expenses = {}

# def add_expense(expenses, category, amount, description):
#     purchase_number = len(expenses)
#     category = category.lower()
#     expenses[purchase_number] = {"category": category, "amount": amount, "description": description}
#     return expenses

# add_expense(total_expenses, "Food", 25, "Burger King")
# add_expense(total_expenses, "Entertainment", 65, "Movies")
# add_expense(total_expenses, "enterainment", 90, "Go Carts")
# add_expense(total_expenses, "entertainment", 150, "top Golf")
# add_expense(total_expenses, "Bills", 2400, "Rent")
# add_expense(total_expenses, "bills", 500, "electric")
# add_expense(total_expenses, "bills", 100, "internet")
# add_expense(total_expenses, "bills", 100, "EZ Pass")
# add_expense(total_expenses, "Food", 12, "Starbucks")
# add_expense(total_expenses, "Food", 12, "Starbucks")
# add_expense(total_expenses, "Food", 12, "Starbucks")

# def simple_expense_list(expenses):
#     for expense in expenses.items():
#         print(expense)

# simple_expense_list(total_expenses)

# def total_spent(expenses):
#     total = 0
#     for _, details in expenses.items(): # learned today to use _ when unpacking a dict and don't need the initial
#         total = total + details["amount"]
#     return f"the total ammount of expenses is:\n {total}"
    
# print(total_spent(total_expenses))

# def spent_by_category(expenses):
#     categorized_expenses = {}
#     for _, details in expenses.items():
#         category = details["category"]
#         amount = details["amount"]
#         categorized_expenses[category] = categorized_expenses.get(category, 0 ) + amount
#     return f"Amount spent by category is:\n {categorized_expenses}"

# print(spent_by_category(total_expenses))

# def most_expensive(expenses):
#     most_expensive_expense = max(expenses, key=lambda description:expenses[description]["amount"])
#     description = expenses[most_expensive_expense]["description"]
#     amount = expenses[most_expensive_expense]["amount"]
#     return f"The Most expensive Item was:\n {description}: {amount}"
    
# print(most_expensive(total_expenses))

# def expenses_over(expenses, amount):
#     list_of_items_costing_more = []
#     for _, details in expenses.items():
#         expense_item = details["description"]
#         expense_amount = details["amount"]
#         if expense_amount > amount:
#             list_of_items_costing_more.append(expense_item)
#     if len(list_of_items_costing_more) == 0:
#         return f"Nothing Costs more than ${amount}"
#     else:
#         return list_of_items_costing_more
    
# print(expenses_over(total_expenses, 24))

# -------------------------------------Cheat sheet------------------------------------------------
# Do I need to loop or not?

# Need ONE specific thing → direct access, no loop
# Need ALL of them → loop

# Do I unpack or not?

# Need BOTH key and value → for key, value in dict.items()
# Need only values → for _, value in dict.items()
# Need only keys → for key in dict
# Already have the key → dict[key]["whatever"]


# # option 1 - declare variables first (readable)
# category = details["category"]
# amount = details["amount"]

# # option 2 - inline (compact)
# categorized[details["category"]] += details["amount"]

# 🐍 Challenge 9 — Mini Store Inventory
# Build a small store inventory system. This one is bigger than the others — it's meant to feel like a real program.
# Data structure — you design it again.
# Functions:
# 1. add_item(inventory, name, price, quantity) — adds an item to the store
# 2. sell_item(inventory, name, quantity) — reduces quantity when something sells, errors if not enough stock or item doesn't exist
# 3. restock_item(inventory, name, quantity) — increases quantity of existing item, errors if item doesn't exist
# 4. total_inventory_value(inventory) — returns total value of all stock combined (price × quantity for each item)
# 5. low_stock(inventory) — returns list of items with quantity 5 or below
# 6. most_valuable_item(inventory) — returns the item with the highest total value (price × quantity)

# mini_store_inventory = {} 

# def add_item(inventory, name, price, quantity):
#     name = name.lower()
#     inventory[name] = {"price": price, "quantity":quantity}
    
# add_item(mini_store_inventory, "milk - 2%", 3.99, 10)
# add_item(mini_store_inventory, "Energy Drink - Monster", 2.99, 40)
# add_item(mini_store_inventory, "Energy Drink - Red Bull", 2.99, 40)
# add_item(mini_store_inventory, "donut - glazed", .99, 5)
# add_item(mini_store_inventory, "Donut - plain", .99, 5)
# add_item(mini_store_inventory, "donut - chocolate glazed", .99, 8)
# add_item(mini_store_inventory, "medicine - aspirin", 5.99, 25)

# def simple_inventory_check(inventory):
#     print("Currently in Stock:")
#     for item, details in inventory.items():
#         print(item,":",details)

# simple_inventory_check(mini_store_inventory)

# def sell_item(inventory, item, quantity):
#     try:
#         item = item.lower()
#         if item in inventory:
#             if inventory[item]["quantity"] >= quantity:
#                 inventory[item]["quantity"] = inventory[item]["quantity"] - quantity
#             else:
#                 return "not enough stock"
#         else:
#             return f"{item} not found"
#     except TypeError:
#         print("Quantity should be an integer")
    
# print("Lets check to see if the sell_item works :P")
# sell_item(mini_store_inventory, "milk - 2%", 3)
# sell_item(mini_store_inventory, "milk - 2%", "one")

# simple_inventory_check(mini_store_inventory)

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

# nums = [1, 2, 2, 3, 4, 4]

# unique = set(nums)
# print(unique)

# problem  - return true if there's any duplicates

# my_list = [1, 3, 'jon', 'james', 15, 'kickboxing', 'yes', 'no', 'yes']

# # def check_for_dupes(my_input):
# #     if len(my_input) != len(set(my_input)):
# #         return True
# #     else:
# #         return False
    
# # refractured
# def check_for_dupes(my_input):
#     return len(my_input) != len(set(my_input))
    
# print(check_for_dupes(my_list))

# week 1 Review 

# new month same challenges

# 🐍 Challenge 9 — Mini Store Inventory
# Build a small store inventory system.
# 1. add_item(inventory, name, price, quantity) — adds item, name should be lowercased
# 2. sell_item(inventory, name, quantity) — reduces quantity when sold, handle: item not found, not enough stock, wrong input type
# 3. restock_item(inventory, name, quantity) — increases quantity, handle: item not found
# 4. total_inventory_value(inventory) — returns total value of ALL stock (price × quantity for each item, added together)
# 5. low_stock(inventory) — returns list of items with quantity 5 or below
# 6. most_valuable_item(inventory) — returns item with highest total value (price × quantity)

# mini_store = {}

# def add_item(inventory, name, price, quantity):
#         name = name.lower()
#         inventory[name] = {"price": price, "quantity": quantity}
#         return inventory

# add_item(mini_store, "Monster", 2.99, 20)
# add_item(mini_store, "Red Bull", 2.99, 30)
# add_item(mini_store, "Milk 2%", 4.99, 10)
# add_item(mini_store, "Milk Chocolate", 1.99, 25)
# add_item(mini_store, "Monster Rehab - Berry Tea", 2.99, 45)
# add_item(mini_store, "Milk Strawberry", 1.99, 50)
# add_item(mini_store, "Doritos", 2.50, 68)


# def simple_inventory_list(inventory):
#         for name, details in inventory.items():
#                 print(name, details)

# simple_inventory_list(mini_store)

# def sell_item(inventory, name, sold_ammount):
#         if name in inventory:
#                 current_ammount = inventory[name]["quantity"]
#                 if current_ammount > 0 and sold_ammount < current_ammount:
#                         inventory[name]["quantity"] = current_ammount - sold_ammount
#                 else:
#                         return "Either not enough in stock or too much sold"
#         else:
#                 return f"{name} not in inventory"
        
# def restock_item(inventory, name, amount_stocked):
#         if name in inventory:
#                 current_ammount = inventory[name]["quantity"]
#                 inventory[name]["quantity"] = current_ammount + amount_stocked
#         else:
#                 return f"{name} is not in your inventory - please add properly first"
        
# def total_inventory_value(inventory):
#         total = 0
#         for _, details in inventory.items():
#                 total = total + (details["price"] * details["quantity"])
#         return f"total amount of inventory: ${total:.2f}" # adding the :.2f floats decimal to tenths

# print(total_inventory_value(mini_store))

# def low_stock(inventory):
#         low_stock = []
#         for name, details in inventory.items():
#                 stock = details["quantity"]
#                 if stock <= 5:
#                         low_stock.append(name)
#         return low_stock

# def most_valuable_item(inventory):
#         most_val = max(inventory, key=lambda name: inventory[name]["price"] * inventory[name]["quantity"])
#         return f"the most valuable thing in stock is {most_val}"

# print(most_valuable_item(mini_store))
        
#                 🐍 Challenge 10 — Password Validator
# Write a function called validate_password(password) that checks if a password meets these requirements:
# 1. At least 8 characters long
# 2. Contains at least one uppercase letter
# 3. Contains at least one lowercase letter
# 4. Contains at least one number
# 5. Contains at least one special character from this list: !@#$%^&*
# Return a list of everything that's WRONG with the password. If the list is empty, return "Password is valid!" If not, return the list of failures.

# def validate_password(password):
#     total_count = 0
#     total_upper = 0
#     total_lower = 0
#     total_int = 0
#     total_special = 0
#     special_char = "!@#$%^&*"
#     list_of_failures = []
#     for char in password:
#         total_count += 1
#         if char.isupper():
#             total_upper += 1
#         elif char.islower():
#             total_lower += 1
#         elif char.isdigit():
#             total_int += 1
#         elif any(item in special_char for item in char):
#             total_special += 1
#     if total_count < 8:
#         list_of_failures.append("Not ennough characters - needs to be at least 8 characters long")
#     if total_upper < 1:
#         list_of_failures.append("Password must use one uppercase Letter")
#     if total_lower < 1:
#         list_of_failures.append("Password must contain one lowercase Letter")
#     if total_int < 1:
#         list_of_failures.append("Password must contain one number")
#     if total_special < 1:
#         list_of_failures.append("Password must have one special character !@#$%^& ")
#     if len(list_of_failures) == 0:
#         return "Password Accepted"
#     else:
#         return list_of_failures

# print((validate_password("Check!#")))


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

# def valid_parentheses(string):
#     # Something to hold our check
#     stack = []
#     # loop through the string
#     for symbol in string:
#         # check for opening
#         if symbol == "(":
#             # if there is the opening add to our check list
#             stack.append(symbol)
#         # if the symbol closes
#         elif symbol == ")":
#             # check if list is empty -
#             if len(stack) == 0:
#                 # return false  
#                 return False
#             # else pop out the opening we saved -
#             else:
#                 stack.pop()
#     # if check list is empty then we know it opened and closed enough to clear out
#     return len(stack) == 0
    
# print(valid_parentheses("((()))"))
# print(valid_parentheses("(())))"))
# print(valid_parentheses(")))"))
# print(valid_parentheses("((()))"))



# Problem 1
# Write a function called most_frequent_element that takes a list and returns the element that appears most frequently. If there's a tie, return the one that appears first in the list.
# Input: [1, 3, 2, 1, 4, 3, 1]
# Output: 1

# Input: [5, 5, 4, 4]
# Output: 5

# def most_frequent_element(list_of_nums):
#     # create dict to hold count of numbers
#     number_count = {}
#     # iterate through our list
#     for num in list_of_nums:
#         # count our numbers in our dict
#         number_count[num] = number_count.get(num, 0) + 1
#      # store our highest
#     most_common = max(number_count.values())
#     #loop and find what has most common
#     for number, count in number_count.items():
#         # compare the count to the most common (max)
#         if count == most_common:
#             # actual number that has the most common occurencnces
#             return number

# print(most_frequent_element([1, 3, 2, 1, 4, 3, 1]))
# print(most_frequent_element([5, 5, 4, 4]))
# print(most_frequent_element([4, 1, 2, 1, 2, 3, 5]))

# Problem 2
# Write a function called reverse_words that takes a sentence and returns the sentence with the words in reverse order.
# Input: "Hello my name is Jonathan"
# Output: "Jonathan is name my Hello"

# Input: "I love coding"
# Output: "coding love I"

# def reverse_words(string):
#     # split the words
#     word_split = string.split()
#     # reverse the list
#     reverse_it = word_split[::-1]
#     # return and join it
#     return (" ").join(reverse_it)

# print(reverse_words("I love coding"))

# Problem — find_missing_number
# Write a function that takes a list of numbers from 1 to n with one number missing and returns the missing number.

# def missing_number(nums):
#     # find what n actually is
#     n = max(nums)
#     # calculate expected sum
#     expected = n * (n + 1) // 2
#     # calculate actual sum
#     actual = sum(nums)
#     # the difference is the missing number
#     return expected - actual

# print(missing_number([1, 3, 4, 5, 6, 7]))
# print(missing_number([2, 3, 4, 5, 6, 7]))
    
# print(validate_password("hello"))          # fails multiple
# print(validate_password("Hello1!"))        # valid
# print(validate_password("hello1!"))        # fails uppercase
# print(validate_password("HELLO1!"))        # fails lowercase
# print(validate_password("Helloworld!"))    # fails number

# 1. reverse_string(s) — return the string reversed
# 2. every_other(s) — return every other character starting from index 0
# 3. first_half(s) — return the first half of the string
# 4. last_three(s) — return the last 3 characters
# 5. palindrome_check(s) — return True if the string is the same forwards and backwards

# def reverse_string(string):
#     return string[::-1]

# def every_other(string):
#     return string[0::2]

# def first_half(string):
#     half = len(string)//2 # // = no float
#     return string[0:half]

# def last_three(string):
#     return string[-3::]

# def palindrome_check(string):
#     return string == string[::-1]

# print(reverse_string("hello"))        # "olleh"
# print(every_other("abcdefg"))       # "aceg"
# print(first_half("abcdefgh"))         # "abcd"
# print(last_three("jonathan"))         # "han"
# print(palindrome_check("racecar"))    # True
# print(palindrome_check("hello"))      # False

# 1. Given a list of numbers, return only the even ones
# 2. Given a list of words, return only words longer than 4 characters
# 3. Given a list of numbers, return each number squared
# 4. Given a list of words, return them all uppercase
# 5. Given a list of numbers, return only numbers divisible by 3 but not by 9

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 27]
# words = ["cat", "elephant", "dog", "python", "rat", "javascript"]

# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)

# words_over_4 = [word for word in words if len(word) > 4]
# print(words_over_4)

# nums_squared = [num ** 2 for num in numbers]
# print(nums_squared)

# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)

# divis_by_3_not_9 = [num for num in numbers if num % 3 == 0 and num % 9 != 0]
# print(divis_by_3_not_9)

students = [
    {"name": "Jon", "subject": "math", "score": 88},
    {"name": "Emma", "subject": "science", "score": 95},
    {"name": "Bob", "subject": "math", "score": 72},
    {"name": "Sara", "subject": "science", "score": 91},
    {"name": "Mike", "subject": "math", "score": 95},
    {"name": "Lisa", "subject": "science", "score": 78},
    {"name": "Alex", "subject": "math", "score": 65},
]

Write these functions:
1. top_scorer(students) — return the student with the highest score using max() and lambda
2. subject_averages(students) — return a dict of average score per subject using .get() accumulation
3. passing_students(students) — list comprehension, score >= 75
4. rank_students(students) — return students sorted highest to lowest score using sorted() and lambda