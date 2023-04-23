# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 18:57:51 2022

@author: djoke
"""

#Q.1 Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# =============================================================================
#Using zip()
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new = dict(zip(keys,values))
# print(new)
# 
# #Using for loop
# new = dict()
# for i in range(len(keys)):
#     new.update({keys[i]: values[i]})
# print(new)
# 
# =============================================================================

#Q.2 Merge two Python dictionaries into one

# =============================================================================
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# #Approch 1
# print(dict1|dict2)
# 
# #Approch 2
# dict3 = dict2.copy() #First we store copy of dict2 in dict3 
# print(dict3)
# dict3.update(dict1) #Then we update dict3 and storr dict1 to in it.
# print(dict3)
# =============================================================================


#Q.3 Print the value of key ‘history’ from the below dict
# =============================================================================
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# 
# print(sampleDict['class']['student']['marks']['history'])
# =============================================================================


#Q.4 In Python, we can initialize the keys with the same values.

#Given:

# =============================================================================
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# #Expected output:
# 
# #{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
# 
# #Approch 1 (using fromkeys() method)
# #res = dict.fromkeys(employees,defaults)
# #print(res)
# 
# #Approch2
# D = {key:defaults for key in employees}
# print(D)
# 
# #individual data
# #print(res["Kelly"])
# =============================================================================


#Q.5 Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

#Given dictionary:
# =============================================================================
# 
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# 
# # Keys to extract
# keys = ["name", "salary"]
# 
# new = {}
# for i in keys:
#     if i in sample_dict:
#         new.update({i:sample_dict[i]})
# print(new)
# =============================================================================

#Q.6 Delete a list of keys from a dictionary
#Given:

# =============================================================================
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# 
# # Keys to remove
# keys = ["name", "salary"]
# 
# 
# for i in keys:
#     if i in sample_dict:
#         del sample_dict[i]
# print(sample_dict)
# =============================================================================


#Q.7 Check if a value exists in a dictionary
#We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

#Write a Python program to check if value 200 exists in the following dictionary.

#Given:
# =============================================================================
# 
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("200 is present in the sample_dict")

# =============================================================================


#Q.8 Write a program to rename a key city to a location in the following dictionary.

#Given:

# =============================================================================
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# #Expected output:
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
# 
# del sample_dict['city']
# sample_dict['location'] = "New york"
# print(sample_dict)
# =============================================================================
# Another approch
#sample_dict["location"] = sample_dict.pop('city')


#Q.9 Get the key of a minimum value from the following dictionary
# =============================================================================
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# } 
# 
# print(min(sample_dict, key=sample_dict.get))
# =============================================================================


#Q.10  Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.

#Given:

# =============================================================================
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# 
# 
# sample_dict['emp3']['salary'] = '8500'
# print(sample_dict)
# =============================================================================



