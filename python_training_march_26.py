# 3/6/26 
# problem - find the most common character in a string using Collections.counter

from collections import Counter

string1 = 'this is my string'
string2 = 'this is going to be a longish kind of string to test things'

def find_most_used(text):
    counts = Counter(text.replace(" ",""))
    print(counts.most_common(1))

find_most_used(string1)
find_most_used(string2)

