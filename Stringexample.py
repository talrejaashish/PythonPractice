# 1. Write a program to create  a new string made of an input string's first, middle, and last character.

# str1 = "James"
# print("Orignal string is :",str1)

# # Get first character
# res = str1[0]   #res=J
# # Get string size
# l = len(str1)
# # Get middle index number
# mi = int(l/2) 
# # Get middle character and add it to result
# res = res + str1[mi] #res=Jm
# # Get last character and add it to result
# res = res + str1[l-1] #res=Jms
# print("New string :",res)

# 2. Write a program to create a new string made of the middle three characters of an input string.

# def get_middle_three_chars(str1):
#     print("Orignal String is :",str1)

#     mi = int(len(str1)/2)
#     res = str1[mi-1:mi+2]
#     print("Middle three chars are :",res)
# a = input("Enter a name or someting :")
# get_middle_three_chars(a)

# 3. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# s1 = input('Enter a string :')
# s2 = input("Enter a string :")
# mi = int(len(s1)/2) #middle index number of s1
# x = s1[:mi:] #Get character from 0 to the middle index number from s1
# x = x + s2 #concatenate s2 to it
# x = x + s1[mi:] #append remaining character from s1
# print("After appending new string in middle :",x)
# 4. Create a new string made of the first, middle, and last character of each input string

# s1 = "America"
# s2 = "Japan"

# res = s1[0] + s2[0]
# mi_s1 = int(len(s1)/2) 
# mi_s2 = int(len(s2)/2)
# res = res + s1[mi_s1]+s2[mi_s2] + s1[-1] +s2[-1]
# print(res)

# 5. Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# from ntpath import join
# s = input("Enter a word or something :")
# lower = [] #Create a list 
# upper = []
# for i in s: #Iterate each element of the list
#     if i.islower():
#         lower.append(i) #add lowercase character to lower list
#     else:
#         upper.append(i)
## Join both list
# c = ''.join(lower+upper)
# print(c)

# 6. Count all letters, digits, and special symobols from a given string.

# s = input("Enter a string :")
# char = 0
# digit = 0
# symbol = 0
# for i in s:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         symbol +=1 
# print("Total counts of chars, digits, and symobols\nChars =",char,"\nDigits =",digit,"\nSymbol =",symbol)

# 7. Given two strings, s1 and s2. Write a program to create a new string s3 made of the first car of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

# Method 1
# s1 = 'Abc'
# s2 = "Xyz"
# res = s1[:1] + s2[-1] + s1[1:2] + s2[-2] + s1[-1] + s2[:1]
# print(res)

# Method 2
# s1 = "Abc"
# s2 = "Xyz"
# s1_length = len(s1)
# s2_length = len(s2)
# length = s1_length if s1_length > s2_length else s2_length
# result = ""
# s2 = s2[::-1] # Reverse s2 so we can take it in our program in reverse
# for i in range(length):
#     if i<s1_length:
#         result = result + s1[i]
#     if i<s2_length:
#         result = result + s2[i]
# print(result)

# 8. Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character's position doesn't matter.

# s1 = 'Yn'
# s2 = "PYnative"
# a = True
# b = False
# if s1 in s2:
#     print(a)
# else:
#     print(b)

# Using Function

# def test(s1,s2):
#     flag = True
#     for i in s1:
#         if i in s2:
#             continue
#         else:
#             flag = False
#     return flag
# s1 = input("Enter a substring :")
# s2 = input("Enter a whole string :")
# flag = test(s1,s2)
# print("Balanced :",flag)

# 9. Write a program to find all occurrences of "USA" in a given string ignoring the case.

# s = "Welcome to USA. usa awesome, isn't it?"
# a = s.lower()
# b = 'usa'
# print("The usa count is :",a.count(b))

# 10. Given a string s1, write a program to return the sum and average of the digits that appeat in the string, ignoring all other characters.

# s = "PYnative29@#8496"
# sum = 0
# a = 0
# for i in s:
#     if i.isdigit():
#         a +=1
#         sum = sum+int(i)
# avg = sum/a
# print('Sum is:',sum,"Average is :",avg)

# 11. Write a program to count occurrences of all characters within a string

#Method 1
# a = "Apple"
# for i in a:
#     print(i,":",a.count(i))

# Method 2
# s = "Apple"
# c_dict = dict()
# for i in s:
#     count = s.count(i)
#     c_dict[i]=count
# print("Result :",c_dict)

# 12. Reverse a given string

# s = input("Enter a string :")
# print(s[::-1])
# #2nd method
# s = ''.join(reversed(s))
# print(s)

# 13. Write a program to find the last position of a substring "Emma" in a given string.

# str = "Emma is a data scientist who knows Python. Emma works at google. "
# print("Orignal string is :",str)
# index = str.rfind("Emma")
# print("Last occurence of Emma starts at index :",index)

# 14. Write a program to split a given string on hyphens and display each substring.
# str = "Emma-is-a-data-scientist"
# a = str.split("-")
# print(a)
# for i in a:
#     print(i)

# 15. Remove empty strings from a list of strings
# Method 1 (Using the builtin function filter())
# str = ["Emma",'Jon','','Kelly',None,'Eric','']
# print("Orignal list of string :",str)
# new = list(filter(None,str))
# print(new)

# Method 2 (Using the loop and if condition)
# str = ["Emma",'Jon','','Kelly',None,'Eric','']
# new = []
# for i in str:
#     if i:
#         new.append(i)
# print(new)

# 16. Remove special symobols/punctuation from a string

# import re

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# # replace special symbols with ''
# res = re.sub(r'[^\w\s]', '', str1)
# print("New string is ", res)












