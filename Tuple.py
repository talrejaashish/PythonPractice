"""Tuple : Tuple are ordered collections of heterogeneous data that are unchangeable.Hetrogenous means tuple can store variable of all types.

Characterstics of Tuple
1. Ordered
2. Heterogenous
3. Unchangable
4. Contains duplicate
"""

#Creating a Tuple 
#1. Using parenthesis ()
#2. tuple() constructor

#number tuple
# number_tuple = (10,20,25.75)
# print(number_tuple)

# #string tuple
# string_tuple = ('Jessa','Emma','Kelly')
# print(string_tuple)

# #mixed
# sample_tuple = ('Jessa',30,45.5,[25,78])
# print(sample_tuple)

# #Creating by tuple constructor
# sample_tuple1 = tuple(('Jessa',30,45.5,[23,78]))


# a = tuple(('Jesssa',30,45.5,[25,78]))
# print(a)


#Creating a tuple with a single item
# single_tuple = ('Hello',)
# print(type(single_tuple))

#packing variables into tuple
# t = 1,2,'Hello'
# print(type(t))


#unpacking
# tuple1 = 1,2,"Hello"
# i,j,k = tuple1
# print(i,j,k)


# Length of a Tuple
# tuple = ('P','Y','T','H','O','N')
# print(len(tuple))

# Iterating a tuple
# sample_tuple = tuple((1,2,3,"Hello",[4,8,16]))
# for i in sample_tuple:
#     print(i)

# Indexing
# tuple1 = ('P','Y','T','H','O','N')
# for i in range(4):
#     print(tuple1[i])

# tuple1 = ('P','Y','T','H','O','N')
# print(tuple1[9])


# tuple1 = ('P','Y','T','H','O','N')
# print(tuple1[2.0])

# tuple1 = ('P','Y','T','H','O','N')
# print(tuple1[-1])
# for i in range(-6,0):
#     print(tuple1[i],end="")

# tuple1 = (0,1,2,3,4,5,6,7,8,9,10)
# print(tuple1[1:5])

# Finding an item in a Tuple

# tuple1 = (10,20,30,40,50)
# position = tuple1.index(30)
# print(position)

# tuple1 = (10,20,30,40,50,60,70,80)
# position = tuple1.index(10,4,6)
# print(position)

# tuple1 = (10,20,30,40,50,60)
# print(500 in tuple1)

# tuple1 = (0,1,2,3,4,5)
# print("Tuple before changes :",tuple1)
# sample_list = list(tuple1)
# sample_list.append(6)
# tuple1 = tuple(sample_list)
# print("Tuple after changes :,",tuple1)

# tuple1 = (10,20,[25,75,85])
# #before update
# print(tuple1)

# tuple1[2][0] = 250
# #after update
# print(tuple1)

#Remove items from a tuple
#1. By converting it into a list
#2. Using del keyword

# tuplelist1 = (0,1,2,3,4,5)
# sample_list = list(tuplelist1)
# sample_list.remove(1)
# tuplelist1 = tuple(sample_list)
# print(tuplelist1)

# sampletuple1 = (0,1,2,3,4,5,6,7,8,9,10)
# del sampletuple1
# print(sampletuple1)

# Count the occurence of an item in a tuple

# tuple1 = (10,20,60,30,60)
# count = tuple1.count(60)
# print(count)

# tuple1 = (0,1,2,3,4,5)

# #copy
# tuple2 = tuple1
# print(tuple2)

#Concatenate
# tuple1 = (0,1,2,3,4,5)
# tuple2 = (0,1,1,3,9,5)
# # tuple3 = tuple1+tuple2
# # print(tuple3)

# tuple3 = sum((tuple1,tuple2),())
# print(tuple3)

# Nested tuple
# nested_tuple = ((20,40,60),(10,30,50),'Python')
# print(nested_tuple[2][0])

# for i in nested_tuple:
#     print("tuple",i,"element")
#     for j in i:
#         print(j,end=",")
#     print("\n")



















