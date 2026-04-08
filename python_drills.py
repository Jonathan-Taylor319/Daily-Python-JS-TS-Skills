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

mini_store_inventory = {} 

def add_item(inventory, name, price, quantity):
    name = name.lower()
    inventory[name] = {"price": price, "quantity":quantity}
    
add_item(mini_store_inventory, "milk - 2%", 3.99, 10)
add_item(mini_store_inventory, "Energy Drink - Monster", 2.99, 40)
add_item(mini_store_inventory, "Energy Drink - Red Bull", 2.99, 40)
add_item(mini_store_inventory, "donut - glazed", .99, 5)
add_item(mini_store_inventory, "Donut - plain", .99, 5)
add_item(mini_store_inventory, "donut - chocolate glazed", .99, 8)
add_item(mini_store_inventory, "medicine - aspirin", 5.99, 25)

def simple_inventory_check(inventory):
    print("Currently in Stock:")
    for item, details in inventory.items():
        print(item,":",details)

simple_inventory_check(mini_store_inventory)