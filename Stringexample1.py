"""
Dictionaries : Dictionaries are unordered collections of unique values stored in pairs.
Characterstics of dictionaries
1. Unordered
2. Unique
3. Mutable
Creating a dictionary:
1. a = {"name":"Anubhav","country":"India"}
2. a = dict({"name":"Anubhav"})
3. a = dict([("name","mark"),("country","India")])
# a = {"name":"Jacky",10:"Mobile"}
# a = {"name":"Jacky","tel.":[113,3333,444]}
"""
#Create a empty dictionary
# empty_dict = {}
# print(type(empty_dict))

# person = {"name":"Baanu","country":"India","telephone":1232}
# # access value using key name in []
# print(person['name'])
# get key value using key name in get()
# print(person.get('country'))

#Get all keys
# print(person.keys())
# print(type(person.keys())) 

#Get all values
# print(person.values())
# print(type(person.values()))

# Get all key-value pair
# print(person.items())
# print(type(person.items()))

# Iterating the dictionary using for-loop
# print('key',':','value')
# for key in person:
#     print(key,":",person[key])

# using items() method
# print('key',":",'value')
# for key_value in person.items():
#     #first is key and second is value
#     print(key_value[0],":",key_value[1])

# Find a length of a dictionary 
# print(len(person))

# update dictionary by adding 2 new keys
# person['weight']= 50
# person.update({"Height":6})
# print(person)
# person.update([("city","Delhi"),("company","Tata")])
# print(person)

# Set a default value to a key
# person_details = {"name":"Anubhav","country":"India","telephone":1212}
# # set default value if key doesn't exists
# person_details.setdefault('state','MP')
# #key doesn't exists and value not mentionded. default None
# person_details.setdefault("zip")
# # Key exists and value mentioned. doesn't change value
# person_details.setdefault('country','Canada')
# # Display dictionary
# for key, value in person_details.items():
#     print(key,":",value)

# person = {"name":"Anubhav","country":"India","telephone":1212}
# #updating the country name 
# person["country"]="Canada"
# #print the updated country
# print(person['country'])

#remove last inserted item from the dictionary
# deleted_item = person.popitem()
# print("Deleted item :",deleted_item)
# print(person)

# deleted_item = person.pop('name')
# print("Deleted item :",deleted_item)
# print(person)

# delete key
# del person['name']
# print(person)

#remove all item
# person.clear()
# print(person)

#Del person
# del person
# print(person)

# Checking if a key exists
# key_name = "country"
# if key_name in person.keys():
#     print("country name is",person[key_name])
# else:
#     print("Key not found")

# Join Two Dictionary
# dict1 = {'Jessa':70,"Abhay":20,"Anubhav":21}
# dict2 = {'essa':70,"Abhi":20,"Anu":21}
# # copy second dictionary into first dictionary
# dict1.update(dict2)
# print(dict1)
# # print(dict2)

# #Using **kwargs to unpack
# student_dict1 = {'Abhi':1,'Anu':2}
# student_dict2 = {'Abhiq':5,'Anub':4}
# student_dict3 = {'Abhia':7,'Anuviya':9}

# #Join three dictionaris
# student_dict = {**student_dict1,**student_dict2,**student_dict3}
# print(student_dict)

# dict1 = {'Jessa':70,"Arun":23,'Emma':55}
# dict2 = {'Jass':70,"Aru":23,'Emma':66}
# dict1.update(dict2)
# print(dict1)

# Copy a dictionary

# dict1 = {'c':45,'b':95,'a':35}
# #copy dictionary using copy method
# # dict2 = dict1.copy()
# # print(dict2)
# # dict constructor
# # dict3 = dict(dict1)
# # print(dict3)
# # dict2 = dict1
# # dict2.update({'Jessa': 90})
# # print(dict2)
# print(sorted(dict1.items()))
# print(sorted(dict1))
# print(sorted(dict1.values()))

#Nested dictionary
# address = {'state':'MP','city':'Dun'}
# person = {'name':'Kunal','company':'Google','address':address}
# print('person:',person)

# print('city:',person['address']['city'])

# print("Person details")
# for key,value in person.items():
#     if key=="address":
#         print("Person Address")
#         for nested_key,nested_value in value.items():
#             print(nested_key,":",nested_value)
#     else:
#         print(key,":",value)

#multiple dictionaries signal dict
# each dictionary will store data of a single student
# jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
# emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
# kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}
# class_six = {'student1':jessa,'student2':emma,'student3':kelly}

# print("Student 3 name:",class_six['student3']['name'])
# print("Student 3 marks:",class_six['student3']['marks'])
# #Iterating outer dictionary
# print("\nClass details\n")
# for key,value in class_six.items():
#     print(key)
#     for nested_key,nested_value in value.items():
#         print(nested_key,":",nested_value)
#     print('\n')

#max() and min()
# dict = {1:'aaa',2:'bbb',3:'ccc'}
# print("Maximum Key :",max(dict))
# print("Minimum Key :",min(dict))

#all()
#Both true
# dict1 = {1:'True',1:'False'}
# #One False
# dict2 = {0:'True',1:'False'}
# #Empty dic
# dict3 = {}
# #
# dict4 = {'0':False}
# print('All True Keys :',all(dict1))
# print("One False key",all(dict2))
# print("Empty Dictionary :",all(dict3))
# print("With 0 in single quotes",all(dict4))

#any()






#Exersise 1: Write a python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value.
# keys = ['Ten','Twenty','Thirty']
# values = [10,20,30]
# #Output : {'Ten':10,'Twenty':20,'Thirty':30}
# res_dict = dict()
# for i in range(len(keys)):
#     res_dict.update({keys[i]:values[i]})
# print(res_dict)

#Exersise 2 : Merge two dictionaries
# dict1 = {'Ten':10,'Twenty':20,'Thirty':30}
# dict2 = {'Ten':10, 'Fourty':40,'Fifty':50}
# dict3 = {**dict1,**dict2}
# print(dict3)

#Exersise 3 Intialize dictionary with default values
# employees = ['Kelly','Nisha']
# defaults = {'designation':'Developer','salary':8000}
# #{'Kelly':{'designation':'Developer','salary':8000},'Nisha':{'designation':'Developer','salary':8000}
# res = dict.fromkeys(employees,defaults)
# print(res)

# Write a python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# sample_dict = {
#     "name":"Kelly",
#     "age":25,
#     "salary":8000,
#     "city":"New york"}
# # Keys to extract
# keys = ["name","salary"]
# # {'name':"Kelly","salary":8000}
# res = dict()
# for i in keys:
#     res.update({i:sample_dict[i]})
# print(res)

# Delete a list of keys from a dictionary
# sample_dict = {
#     "name":"Kelly",
#     "age":25,
#     "salary":8000,
#     "city":"New york"}
# # Keys to remove
# keys = ["name","salary"]
#{'city':'New york','age':25}
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)


# sample_dict = {k: sample_dict[k] for k in sample_dict.keys()-keys}
# print(sample_dict)

#Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a':100,'b':200,'c':300}
# #Output: 200 present in a dict
# if 200 in sample_dict.values():
#     print('200 present in a dict.')

# Write a program to rename a key city to a location in the following dictionary.
# sample_dict = {
#     "name":"Kelly",
#     "age":25,
#     "salary":8000,
#     "city":"New york"}
# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

#Get the key of a minimum value from the following dictionary
# sample_dict = {
#     'Physics':82,
#     'Maths': 65,
#     'History':75
# }
# print(min(sample_dict,key=sample_dict.get))

# Write a Python program to change Brad's salary to 8500 in the following dictionary.
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary']=8500
# print(sample_dict)



#Test wheater a python dictionary contains a specific key
# fruits = {}
# fruits["apple"] = 1
# fruits["mango"] = 2
# fruits["banana"] = 4

# # Use in.
# if "mango" in fruits:
#     print("Has mango")
# else:
#     print("No mango")

# # Use in on nonexistent key.
# if "orange" in fruits:
#     print("Has orange")
# else:
#     print("No orange")

#Write a python script to sort (ascending and descending ) a dictionary value
# import operator
# d = {1:2,3:4,4:3,2:1,0:0}
# print("Orignal dictionary :",d)
# sorted_d = sorted(d.items(),key=operator.itemgetter(1))
# print("Dictionary in ascending order by value :",sorted_d)

#Write a python script to add a key to a dictionary
# sample_dict = {0:10,1:20}
# res_dict = {0:10,1:20,2:30}
# sample_dict[2]=30
# print(sample_dict)
# sample_dict.update({2:30})
# print(sample_dict)

# Write a python script to concatenate following dictionaries
"""
sample dictionary :
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
"""





































 
















