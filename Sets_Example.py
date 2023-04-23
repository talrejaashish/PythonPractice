# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 12:38:25 2022

@author: djoke
"""

#Q.1 Given a Python list, Write a program to add all its elements into a given set.

#Given:

# =============================================================================
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# 
# =============================================================================
# =============================================================================
# # Approch 1
# sample_set.update(sample_list)
# print(sample_set)
# 
# # Approch 2
# c = sample_set.union(sample_list)
# print(c)
# 
# # Approch 3
# sample_set = list(sample_set)
# a = sample_set + sample_list
# print(a)
# =============================================================================


#Q.2 Return a new set of identical items from two sets
#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# c = set1.intersection(set2)
# print(c)
# =============================================================================


#Q.3 Write a Python program to return a new set with unique items from both sets by removing duplicates.

#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# 
# set3 = set1.union(set2)
# print(set3)
# =============================================================================



#Q.4 Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

#Given:

# =============================================================================
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)
# =============================================================================


#Q.5 Write a Python program to remove items 10, 20, 30 from the following set at once.

#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2= {10,20,30}
# set1.difference_update(set2)
# print(set1)
# =============================================================================
    
#Q.6  Return a set of elements present in Set A or B, but not both
#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# 
# set1.symmetric_difference_update(set2)
# print(set1)
# =============================================================================


#Q.7 Check if two sets have any elements in common. If yes, display the common elements
#Given:
# =============================================================================
# 
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# if set1.isdisjoint(set2) == False:
#     print(set1.intersection(set2))
# =============================================================================


#Q.8 Update set1 by adding items from set2, except common items
#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)
# =============================================================================


#Q.9 Remove items from set1 that are not common to both set1 and set2
#Given:

# =============================================================================
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# =============================================================================

# =============================================================================
# inter = set1.intersection(set2)
# print(inter)
# =============================================================================
   
# =============================================================================
# set1.intersection_update(set2)
# print(set1)
#             
# =============================================================================

 

