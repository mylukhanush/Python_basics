# Counters:it is used to count the elements
# OrderedDict:it remembers the order in which the keys were inserted.
# DefaultDict:it is used to provide keys if not provided to the values.
# ChainMap:it is used to maintain many dictionaries into a single unit and returns in a list of dictionaries.
# NamedTuple:it returns a tuple object with names for each position which the ordinary tuples lack.
#....Suppose for calling fname instead of remembering the index position you can actually call the element.
# Deque:it is used for quicker append and pop operations from both sides of the container.
# UserDict
# UserList
# UserString



#Counter
# ways to create Counter
# from collections import Counter

# With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
#                'B', 'A', 'C']))

# with dictionary
# print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
# print(Counter(A=3, B=5, C=2))

#OrderedDict
# from collections import OrderedDict
# print("This is a Dict:\n")
# d = {}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# for key, value in d.items():
#     print(key, value)
# print("\nThis is an Ordered Dict:\n")
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
# for key, value in od.items():
#     print(key,value)


# from collections import defaultdict
# d = defaultdict(int)
# L = [1, 2, 3, 4, 2, 4, 1, 2]
# for i in L:
#     d[i] += 1
# print(d)


# defaultdict
# from collections import defaultdict
# d = defaultdict(list)
# for i in range(5):
#     d[i].append(i)
# print("Dictionary with values as list:")
# print(d)


# ChainMap
# from collections import ChainMap
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
# c = ChainMap(d1, d2, d3)
# print(c)

#Adding new dictionary
# import collections
# dic1 = {'a': 1, 'b': 2}
# dic2 = {'b': 3, 'c': 4}
# dic3 = {'f': 5}
# chain = collections.ChainMap(dic1, dic2)
# print("All the ChainMap contents are : ")
# print(chain)
# chain1 = chain.new_child(dic3)
# print("Displaying new ChainMap : ")
# print(chain1)



#Named Tuple
# from collections import namedtuple
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
# S = Student('Nandini', '19', '2541997')
# print("The Student age using index is : ", end="")
# print(S[1])
# print("The Student name using keyname is : ", end="")
# print(S.name)

#Conversion Operations
#1._make()
#2._asdict()
# from collections import namedtuple
# Student = namedtuple('Student',['name','age','DOB'])
# S = Student('Bunny','22','9876543')
# li = ['khanush','23','765432']
# di = {'name':"nikhil",'age':24,'DOB':'2345678'}
# print("The namedtuple instance using iterable is:")
# print(Student._make(li))
# print("The OrderedDict instance using namedtuple is  : ")
# print(S._asdict())

#Deque(Doubly Ended Queue)
#is the optimized list for quicker append and pop operations...
#.....from both sides of the container.
# It provides O(1) time complexity for append and pop operations...
#...as compared to list with O(n) time complexity.
#Syntax:
# class collections.deque(list)


    #Inserting Elements
# from collections import deque
# de = deque([1, 2, 3])
# de.append(4)
# print("The deque after appending at right is : ")
# print(de)
# de.appendleft(6)
# print("The deque after appending at left is : ")
# print(de)

#Removing Elements
# from collections import deque
# de = deque([6, 1, 2, 3, 4])
# de.pop()
# print("The deque after deleting from right is : ")
# print(de)
# de.popleft()
# print("The deque after deleting from left is : ")
# print(de)


#User Dict
