# Write a program to check wheather a given key exists in a dictionary or not.

# dict1 = {'0':1,'1':2,'2':3}
# #check = 2
# # print('2' in dict.keys())
# x = input("Enter a value :")
# if x in dict1.keys():
#     print(True)
# else:
#     print(False)

# Write a program to iterate over dictionary item using for loop.
# dict = {0:'Value 1',1:'Value 2',2:'Value 3'}
# for key,value in dict.items():
#     print(key,":",value)

# Write a program to print only keys of a dictionary.
# dict = {0:'Value 1',1:'Value 2',2:'Value 3'}
# #Expected Output : dict_keys([0,1,2])
# keys = dict.keys()
# print(keys)

# Write a program to print values of a dictionary.
# dict = {0:'Value 1',1:'Value 2',2:'Value 3'}
# print(dict.values())

# Write a program in python to map 2 lists into a dictionary.
# keys = [1,2,3]
# values = ['value1','value2','value3']

# #zip function 
# dict = dict(zip(keys,values))
# print(dict)

# Python program to remove a set of keys.
# dict = {0:'Value 1',1:'Value 2',2:'Value 3'}
#keys to remove = [0,1]
# for i in range(2):
#     dict.pop(i)
# print(dict)
# remove = [0,1]
# dict = {k: dict[k]for k in dict.keys()-remove}
# print(dict)

# Python program to sort dictionary by values (Ascending/Descending)
# import operator
# d = {0:'Value 1',1:'Value 2',2:'Value 3'}
# sort_d = sorted(d.items(),key=operator.itemgetter(1),reverse=True)
# print(sort_d)

# Write a program to concatenate two dictionaries to create one.
# dict = {0:'Value 1',1:'Value 2',2:'Value 3'}
# dict1 = {10:'Value 1',4:'Value 2',9:'Value 3'}
# dict3 = {**dict,**dict1}
# print(dict3)

# Write a program to sum all the values of a dictionary.
# dict = {'key1':200,'key2':300,'key3':100}
# sum = 0
# for i in dict.values():
#     sum += i
# print(sum)

# x = []
# for i in dict.values():
#     x.append(i)
# print(sum(x))

# Write a program to get the maximum and minimum value of dictionary.
# dict = {'key1':200,'key2':300,'key3':100}
# val = dict.values()
# max = max(val)
# min = min(val)
# print(max)
# print(min)

# Write a program to check





