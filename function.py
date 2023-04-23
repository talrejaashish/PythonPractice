# Create a function without any parameters

# def message():
#     print("Welcome to my world.")

# message()

# Create a function with parameters
# def courses(name,course_name):
#     print("Hello",name,"Welcome to my world.")
#     print("Your course name is",course_name)

# courses('John','Python')

# Create a function with parameters and return value

# def calculator(a,b):
#     add = a+b
#     return add

# res = calculator(10,4)
# print("Addition :",res)

# Even odd using functions
# def even_odd(n):
#     if n%2==0:
#         print("Even number.")
#     else:
#         print("Odd number.")
# a = int(input('Enter a number :'))
# even_odd(a)

#Docstring(""" """)
# def factorial(x):
#     """This function returns the factorial of a given number."""
#     return x
# print(factorial.__doc__)

# Only even using function
# def is_even(list1):
#     even_num = []
#     for n in list1:
#         if n%2==0:
#             even_num.append(n)
#     return even_num
# even_num = is_even([2,3,5,7,6,8,76,3])
# print("Even numbers are :",even_num)

# Calculator using function
# def calculator(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# x = int(input("Enter a number :"))
# y = int(input("Enter a number :"))
# a,b,c,d = calculator(x,y)
# print("Addition :",a)
# print("Substraction :",b)
# print("Multiplication :",c)
# print("Division :",d)

# The pass statement
# def pass_func():
#     pass
# pass_func()

# Scope(local,global)

# global_lang = 'DataScience'
# def var_scope_test():
#     local_lang = 'Python'
#     print(local_lang)
# var_scope_test()
# print(global_lang)
# print(local_lang)# This will give us name error because it is a local variable

# Local variable
# def func1():
#     loc_var = 790
#     print("Value is :",loc_var)

# def func2():
#     # print("Value is :",local_var) #This will give us error because we cannot use another function local variable in this
#     pass

# func1()
# func2()

# Global varibale

# global_var = 45

# def func1():
#     print("Value in 1st function :",global_var)

# def func2():
#     print("Value in 2nd function :",global_var)
# func1()
# func2()

# Global Keyword

# x = 3
# def function1():
#     print("Value in 1st function :",x)
# def function2():
#     global x
#     x = 232
#     print("Value in 2nd function :",x)
# def function3():
#     print("Value in 3rd function :",x)
# function1() #x=3
# function2() #x=232
# function3() #x=232 because we use global keyword so now we can change it everytime we call it

# nonlocal variable in function(it acts as a global variable for a nested function)

# def outer_func():
#     x = 777

#     def inner_func():
#         nonlocal x # It wil take x as a global variable
#         x = 700
#         print("Value of x inside inner function is :",x)

#     inner_func()
#     print("Value of x inside outer function is :",x)
# outer_func()

# Recursive function

# def factoiral(no):
#     if no==0:
#         return 1
#     else:
#         return no*factoiral(no-1)
# a = int(input("Enter a number :"))
# res = factoiral(a)
# print("The factoial of",a,"is :",res)

#Program for even numbers without lambda function

# def even_numbers(nums):
#     even_list = []
#     for n in nums:
#         if n % 2 == 0:
#             even_list.append(n)
#     return even_list

# num_list = [10, 5, 12, 78, 6, 1, 7, 9]
# ans = even_numbers(num_list)
# print("Even numbers are:", ans)

# Program for even number with a lambda function using filter()
#(filter(function,sequence))

# l = [10, 5, 12, 78, 6, 1, 7, 9]
# even_nos = list(filter(lambda x: x % 2 == 0, l))
# print("Even numbers are: ", even_nos)

#Syntax :map(function,sequence)
#Program of map()
# list1 = [2,3,4,5,3]
# list2 = list(map(lambda x:x*x*x,list1))
# print("Cube values are :",list2)

# Syntax : reduce(function, sequence)
# Program for reduce function
# from functools import reduce


# list1 = [12,3,21,32,3]
# add = reduce(lambda x,y :x+y,list1)
# print("Addition of all list elements is :",add)
