#List Compression:
# Based on a list of fruits, you want a new list, containing
# only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)