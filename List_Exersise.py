# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:32:33 2022

@author: djoke
"""

#Q.1 
#Reverse a list in python.
# =============================================================================
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
# =============================================================================

#Q.2
#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

#Given:

# =============================================================================
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]
# list3 = []
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
# print(list3)
# =============================================================================

# Using list comprehension 
# =============================================================================
# list3 = [list1[i]+list2[i] for i in range(len(list1))]
# print(list3)
# 
# =============================================================================

#Q.3
#Turn every item of a list into its square
#Given a list of numbers. write a program to turn every item of a list into its square.

#Given:

# =============================================================================
# =============================================================================
# numbers = [1, 2, 3, 4, 5, 6, 7]
# new = []
# for i in range(len(numbers)):
#     new.append(numbers[i]**2)
# #     
# print(new)
# 
# # Using list comprehension
# 
# new = [numbers[i]**2 for i in range(len(numbers))]
# print(new)
# # =============================================================================
# =============================================================================

#Q.4
# =============================================================================
# #Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# #Expected output:
# 
# #['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# res = []
# for x in list1:
#     for y in list2:
#         res.append(x+y)
# print(res)
# =============================================================================

#Q.5 
#Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in #original order and items from list2 in reverse order.

#Given

# =============================================================================
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# length = len(list2)
# for i in range(length):
#     print(list1[i],list2[i])
# =============================================================================

#Q.6
# =============================================================================
# #Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1.remove("") 
# list1.remove('')
# print(list1)
# 
# #Approch 2 using filter
# list1 = list(filter(None, list1))
# print(list1)
# =============================================================================

#Q.7
#Write a program to add item 7000 after 6000 in the following Python List

#Given:

# =============================================================================
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # list1[0] = 10
# # list1[1] = 20
# # list1[2] = [300, 400, [5000, 6000], 500]
# # list1[2][2] = [5000, 6000]
# # list1[2][2][1] = 6000
# list1[2][2].append(7000)
# print(list1)
# =============================================================================

#Q.8
#You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

#Given List:

# =============================================================================
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# 
# # sub list to add
# sub_list = ["h", "i", "j"]
# 
# list1[2][1][2].extend(sub_list)
# print(list1)
# =============================================================================

#Q.9
#Replace list’s item with new value if found.
#You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# =============================================================================
# Using index method
# list1 = [5, 10, 15, 20, 25, 50, 20]
# a = list1.index(20)
# list1[a] = 200
# print(list1)
# =============================================================================

        
# =============================================================================
# Using for loop
# list1 = [5, 10, 15, 20, 25, 50, 20]
# for i in list1:
#     if i==20:
#         a = list1.index(i)
# list1[a] = 200
# print(list1)
# =============================================================================

#Q.10 Given a Python list, write a program to remove all occurrences of item 20.

#Given:

# =============================================================================
# Using remove method
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in list1:
#     if i==20:
#         list1.remove(i)
# print(list1)
# =============================================================================

# =============================================================================
# Using append method
# list1 = [5, 20, 15, 20, 25, 50, 20]
# new = []
# for i in list1:
#     if i!=20:
#         new.append(i)
# print(new)
# =============================================================================

# =============================================================================
# Using list comprehension
# list1 = [5, 20, 15, 20, 25, 50, 20]
# new = [i for i in list1 if i!=20]
# print(new)
# 
# =============================================================================

# =============================================================================
# Using while loop
# list1 = [5, 20, 15, 20, 25, 50, 20]
# 
# while 20 in list1:
#     list1.remove(20)
# print(list1)
# =============================================================================




























    
    