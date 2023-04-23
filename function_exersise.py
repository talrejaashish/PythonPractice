#1. Write a program to create a function that takes two arguments, name and age, and print their value.

# def funct():
#     print("Hello")
# funct()

#2. Write a program to create function func1() to accept a variable length of arguments and print their value.

# def func1(*x): #*x(it's  convert and append the values in tuple)
#     print("Printing values")
#     for n in x: #Using this loop we can access element one by one.
#         print(n)
# func1(20,40)

#3. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# def calculation(a,b):
#     c = a+b
#     d = a-b
#     return c,d
# res = calculation(22,43)
# print(res)

#4. Write a program to create a function show_employee() using the following conditions. 
# a. It should accept employee's name and salary and display both.
# b. If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name,salary=9000):
#     print("Name :",name)
#     print("Salary :",salary)
# details = show_employee('Mohan')

#5. Write a program :
#(a) Create an outer function that will accept two parameters, a and b
#(b) Create an inner function inside an outer function that will calculate the addition of a and b
#(c) At last, an outer function will add 5 into addition and return it

# outer function
# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)

#6. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# def recursive_function(n):
#     if n:
#         return n + recursive_function(n-1)
#     else:
#         return 0

# res =recursive_function(10)
# print(res)

#7. You have a function display_student(name,age) which print name,age. Assign a new name show_student(name,age) to it using the new name.

# def display_students(name,age):
#     print(name,age)
# display_students('Emma',26)
# show_student = display_students
# show_student('Emma',26)

#8. Generate a python list of all the even number between 4 to 30

# print(list(range(4,30,2)))

#9. Find the largest item from a given list
# x = [4,6,8,24,12,2]
# maximum =max(x)
# print(maximum)

# Write a program to find lcm

# def lcm(x,y):
#     if x<y:
#         greater = y
#     else:
#         greater = x
#     while(True):
#         if(greater%x==0) and (greater%y==0):
#             lcm = greater
#             break
#         greater+=1
#     return lcm
# num1 = int(input("Enter a number :"))
# num2 = int(input("Enter a number :"))
# print("The LCM of",num1,"and",num2,"is :",lcm(num1,num2))

# Write a program to find hcf

# def hcf(x,y):
#     if x>y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if((x%i==0)and(y%i==0)):
#             hcf = i
#         else:
#             return hcf
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# print("The HCF of these numbers are :",hcf(a,b))


# Write a program to convert decimal to binary, octal and hexadecimal

# def decimal_into_binary(decimal_1):
#     decimal = int(decimal_1)
#     print("The given decimal number",decimal,"in Binary number is:",bin(decimal))

# def decimal_into_octal(decimal_1):
#     decimal = int(decimal_1)
#     print("The given decimal number",decimal,"in Octal number is:",oct(decimal))

# def decimal_into_hexadecimal(decimal_1):
#     decimal = int(decimal_1)
#     print("The given decimal number",decimal,"in Hexadecimal is:",hex(decimal))

# decimal_1 = int(input("Enter a decimal number :"))
# decimal_into_binary(decimal_1)
# decimal_into_hexadecimal(decimal_1)
# decimal_into_octal(decimal_1)

# Create a program to find ASCII value of character.
# def ascii(a):
#     return ord(a)
# alphabet = input("Enter a alphabet :")
# value = ascii(alphabet)
# print("The ASCII value of",alphabet,"is",ascii(alphabet))

# Create a program to display fibonacci sequence using recurssion

# def recur(n):
#     if n<=1:
#         return n
#     else:
#         return(recur(n-1)+recur(n-2))
# nterms = int(input("How many terms :"))
# if nterms<=0:
#     print("Please enter a positive number")
# else:
#     print("Fibonacci sequence :")
#     for i in range(nterms):
#         print(recur(i))

# Create a program to find factorial of number using recursion

# def rec_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*rec_factorial(n-1)
# num = int(input("Enter a number:"))
# if num<0:
#     print("Sorry,factorial does not exist for negative numbers")
# elif num==0:
#     print("The factorial of 0 is 1")
# else:
#     print("THe factorial of",num,'is',rec_factorial(num))

def lcm(x,y):
    if x<y:
        greater = y
    else:
        greater = x
    while(True):
        if(greater%x==0) and (greater%y==0):
            lcm = greater
            break
        greater+=1    
    return lcm
a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
print("The LCM of",a,"and",b,"is :",lcm(a,b))