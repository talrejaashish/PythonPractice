# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:57:04 2022

@author: djoke
"""
#Q.1 Reverse the tuple
#Given:
# =============================================================================
# 
# tuple1 = (10, 20, 30, 40, 50)
# a = tuple1[::-1]
# print(a)
# =============================================================================


#Q.2 The given tuple is a nested tuple. write a Python program to print the value 20.

#Given:
# =============================================================================
# 
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
# =============================================================================


#Q.3 Unpack the tuple into 4 variables
#Write a program to unpack the following tuple into four variables and display each variable.

#Given:

# =============================================================================
# tuple1 = (10, 20, 30, 40)
# a,b,c,d = tuple1
# print(a),print(b),print(c),print(d)
# =============================================================================


#Q.4 Swap two tuples in Python
#Given:

# =============================================================================
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# print("Tuple1 is :",tuple1)
# print("Tuple2 is :",tuple2)
# tuple1,tuple2 = tuple2,tuple1
# 
# print("Tuple1 is :",tuple1)
# print("Tuple2 is :",tuple2)
# =============================================================================

#Q.5 Create a tuple with single item 50

# =============================================================================
# #single = (50) #This will print it as a integer.\
# single = (50,)
# print(single)
# print(type(single))
# =============================================================================

#Q.6 Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

#Given:

# =============================================================================
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:5]
# print(tuple2)
# =============================================================================


#Q.7 Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

#Given:

# =============================================================================
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)
# =============================================================================

#Q.8 Sort a tuple of tuples by 2nd item
#Given:

# =============================================================================
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# tuple1 = list(tuple1)
# tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
# print(tuple1)
# 
# =============================================================================


#Q.9 Counts the number of occurrences of item 50 from a tuple
# Given:

# =============================================================================
# tuple1 = (50, 10, 60, 70, 50)
# count = 0
# for i in tuple1:
#     if i==50:
#         count+=1
# print(count)
# =============================================================================

# Second Approch
# =============================================================================
# tuple1 = (50, 10, 60, 70, 50)
# count_50 = tuple1.count(50)
# print("The count of number 50 :",count_50)
# =============================================================================


#Q.10 Check if all items in the tuple are the same
#tuple1 = (45, 45, 45, 45)
# =============================================================================
# for i in tuple1:
#     if i==i:
#         print(True)
#         break
# =============================================================================

# =============================================================================
# element = tuple[1]
# for i in tuple1:
#     if i==element:
#         print(True)
# =============================================================================

# =============================================================================
# LIST CONSTRUCTOR

# thisset = set(("apple", "banana", "cherry"))
# thisset1 = tuple(("apple", "banana", "cherry"))
# thisset2 = list(("apple", "banana", "cherry"))
# print(type(thisset))
# print(type(thisset1))
# print(type(thisset2))
# =============================================================================


