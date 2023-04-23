# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 06:30:06 2022

@author: djoke
"""

#Q1. 
#Write a program to create a new string made of an input
#string’s first, middle, and last character. 
# =============================================================================
# 
# input = "AbhayJI"
# first = input[0]
# middle = input[int(len(input)/2)]
# last = input[-1]
# print(first+middle+last)   
# =============================================================================


#Q2.
#Write a program to create a new string made of the middle three characters of
#an input string.

# =============================================================================
# name = "JhonnyDipJhonny"
# middle = int(len(name)/2)
# print(name[middle-1]+name[middle]+name[middle+1])
# =============================================================================

#Q3.
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending
#s2 in the middle of s1.

# =============================================================================
# s1 = "Autom"
# s2 = "Winter"
# middle_of_s1 = int(len(s1)/2)
# print(s1[0:middle_of_s1]+s2+s1[middle_of_s1:])
# =============================================================================

#Q4.
#Given two strings, s1 and s2, write a program to return a new string made of s1 and
#s2’s first, middle, and last characters.

#s1 = "Kelly"
#s2 = "Aully"
# =============================================================================
# first = s1[0] + s2[0]
# middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
# last = s1[-1] + s2[-1]
# print(first+middle+last)
# =============================================================================

#Q5.
#Given string contains a combination of the lower and upper case letters.
#Write a program to arrange the characters of a string so that all lowercase 
#letters should come first.

#name = "AbhayKanwasi"

#new = ""
#for i in name:
#    if i.islower()==True:
#       new = new + i
#for i in name:
#   if i.isupper()==True:
#        new = new+i
#print(new)


# NOTE : This approch have two for loops that makes it complexity high.

# =============================================================================
# upper = []
# lower = []
# for i in name:
#     if i.islower()==True:
#         lower.append(i)
#     else:
#         upper.append(i)
# new = "".join(lower + upper)
# print(new)
#         
# =============================================================================

#Q.6
#Count all letters, digits, and special symbols from a given string

# =============================================================================
# new = "123#@_abhay"
# digit = 0
# alphabet = 0
# special_symbol = 0
# for i in new:
#     if i.isdigit()==True:
#         digit+=1
#     elif i.isalpha()==True:
#         alphabet+=1
#     else:
#         special_symbol+=1
# print("Number of digit :",digit)
# print("Number of alphabets :",alphabet)
# print("Number of special symbol :",special_symbol)
# =============================================================================

#Q.7
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the
#first char of s1, then the last char of s2, Next, the second char of s1 and second 
#last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = "Kelly"
s2 = "Aullyra"

# Approch1
#print(s1[0]+s2[-1]+s1[1]+s2[-2]+s1[2]+s2[-3]+s1[3]+s2[-4]+s1[4]+s2[-5])

# Approch 2
# =============================================================================
# c = 0
# len_s1 = len(s1)
# len_s2 = len(s2)
# if len_s1 > len_s2:
#     c = c + len_s1
# else:
#     c = c + len_s2
# s2 = s2[::-1]
# result = ""
# for i in range(c):
#     if i < len(s1):
#         result = result + s1[i]
#     if i < len(s2):
#         result = result + s2[i]
# print(result)
# =============================================================================


#Q.8
#Write a program to check if two strings are balanced. For example, strings s1 and s2 
#are balanced if all the characters in the s1 are present in s2. 
#The character’s position doesn’t matter.

# =============================================================================
# s1 = input("Enter a string : ")
# s2 = input("Enter a string : ")
# 
# for i in range(len(s1)):
#     a = s1[i]
#     if a in s2:
#         b = True
#     else:
#         b = False
# print("Result of Balance Test :",b)
# =============================================================================


#Q.9 
# Find all occurence of a substring in a given string by ignoring the case.
# It means write a program to find all occurences of "USA" in a given string ignoring the case.

# =============================================================================
# str1 = "Welcome to USA. usa awesome, isn't it?"
# count = 0
# str1 = str1.lower()
# str2 = "usa"
# if str2 in str1:
#     count+=1
# print(count)
# =============================================================================

#Q.10
#Calculate the sum and average of the digits present in a string
#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring
#all other characters.

# =============================================================================
# str1 = "PYnative29@#8496"
# sum = ""
# num = 0
# for i in str1:
#     if i.isdigit()==True:
#         num += 1
#         sum += i
# 
# c = 0
# for i in sum:
#     i = int(i)
#     c = c + i
# print("The sum of digits is :",c)
# average = c/num
# print("The average of {0} is :".format(c),average)
# =============================================================================

#Q.11
#Write a program to count occurrences of all characters within a string
#Given:

# =============================================================================
# str1 = "Apple"
# 
# # create a result dictionary
# char_dict = dict()
# 
# for char in str1:
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)
# =============================================================================
        
#Q.12
#Reverse a given string.
# =============================================================================
# Using slicing 

# string = input("Enter a string :")
# reverse = string[::-1]
# print(reverse)
# =============================================================================


# Using join() and reversed()
# =============================================================================
# string = input("Enter a string : ")
# len_of_string = len(string)
# strin = ''.join(reversed(string))
# print(strin)
# =============================================================================

#Q.13
#Write a program to find the last position of a substring “Emma” in a given string.


# Approch 1(Using index)
# =============================================================================
# # initializing string
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# # printing original string
# print ("The original string is : " + str1)
# occ = str1.index("Emma",4,100)
# print(occ)
# =============================================================================
# Approch 1 only appplicable when we have this particular string.


# Approch 2 (Using rfind())
# =============================================================================
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)
# 
# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index:", index)
# =============================================================================

#Q.14
#Write a program to split the given string on hypens and display each substring.

# =============================================================================
# str1 = "Emma-is-a-data-scientist"
# str2 = str1.split("-")
# for i in range(len(str2)):
#     print(str2[i])
# =============================================================================

#Q.15
#Write a program to insert a character after every character.

# =============================================================================
# # initializing string
# test_str = "Emma is a data scientiest"
# 
# # printing original string
# print("The original string is : " + test_str)
# 
# # Using join() + list comprehension
# # Insert character after every character pair
# res = '-'.join(test_str[i:i + 1] for i in range(0, len(test_str), 2))
# 
# # printing result
# print("The string after inserting comma after every character pair : " + res)
# =============================================================================

#Q.16
#Remove the empty string from a list of string.

# =============================================================================
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# emove = str_list.remove("")
# emove = str_list.remove('')
# emove = str_list.remove(None)
# print(str_list)
# =============================================================================
    
#Q.17
#Remove special symbol/pancutuation from a string.

# =============================================================================
# str1 = "/*Jon is @developer & musician"
# pancutuation = "!~`@#$%^&*()_-+=?/<,>."
# new_string = ""
# for i in str1:
#     if i not in pancutuation:
#         new_string += i
# print(new_string)
# =============================================================================
        
#Q.18
#Write a program to find words with both alphabets and numbers from an input string.


# =============================================================================
# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)
# 
# res = []
# # split string on whitespace
# temp = str1.split()
# 
# # Words with both alphabets and numbers
# # isdigit() for numbers + isalpha() for alphabets
# # use any() to check each character
# 
# #for item in temp:
# #   if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
# #       res.append(item)
# 
# for i in temp:
#     if any(j.isalpha() for j in i) and any(j.isdigit() for j in i):
#         res.append(i)
# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)
# =============================================================================


#Q.19
#Replace each special symbol with # in the following string
# =============================================================================
# import string
# 
# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)
# 
# # Replace punctuations with #
# replace_char = '#'
# 
# # string.punctuation to get the list of all special symbols
# for char in string.punctuation:
#     str1 = str1.replace(char, replace_char)
# 
# print("The strings after replacement : ", str1)
# =============================================================================

#Q.20
#






















