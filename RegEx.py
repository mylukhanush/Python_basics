#findall,search,split,sub


# The findall() Function
# import re
# txt = "The rain in Spain"
# x = re.findall("in", txt)
# print(x)


# Return an empty list if no match was found:
# import re
# txt = "The rain in Spain"
# x = re.findall("Spain", txt)
# print(x)

# The search() Function
# import re
# txt ="The rain in Spain"
# x = re.search("\s", txt)
# print("The first character is located in position:", x.start())

# import re
# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

#The split() Function
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt, 2)
# print(x)

# The sub() Function
# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "_", txt)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "_", txt, 2)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.escape(txt)
# print(x)

# import re
# print(re.escape("This is Awesome even 1 AM"))
# print(re.escape("I Asked what is this he said "))

# import re
# txt = "A Counter is a container that keeps track of how many times equivalent values are added. It is part of the collections module in Python and is a subclass of the built-in dict class. Counter objects are dictionaries where keys are elements and values are kyu their counts"
# x = re.findall(r'\bk\w*', txt)
# print(x)

# import re
# txt = "Counter objects are dictionaries where keys are elements and values are their counts.my email is host@gmail.com and mobile number is 5689741235."
# x = re.findall(r'\S+@\S+', txt)
# y = re.findall(r"\b\d{10}\b", txt)
# print(x)
# print(y)
