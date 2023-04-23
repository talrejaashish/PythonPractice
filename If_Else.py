# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:17:48 2022

@author: djoke
"""

#Q.1  Write a program to check whether a person is eligible for voting or not. (accept age from user)

# APPROCH 1
# =============================================================================
# age = int(input("Enter your age :"))
# if age>=18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
# =============================================================================

# APPROCH 2
# =============================================================================
# age = int(input("Enter your age : "))
# print("You are eligibel to vote.") if age>=18 else print("You are not eligible to vote.")
# =============================================================================


#Q.2 Write a program to check whether a number entered by user is even or odd.

# APPROCH 1
# =============================================================================
# num = float(input("Enter a number :"))
# if num%2==0:
#     print("{0} is a even number".format(num))
# else:
#     print("{0} is a odd number.".format(num))
# =============================================================================

# APPROCH 2
# =============================================================================
# num = int(input("Enter a number :"))
# print("{0} is a even number.".format(num)) if num%2==0 else print("{0} is a odd number.".format(num))
# =============================================================================


#Q.3  Write a program to check whether a number is divisible by 7 or not.

# APPROCH 1
# =============================================================================
# num = int(input("Enter a number :"))
# if num%7==0:
#     print("The number is divisible by 7.")
# else:
#     print("The number is not divisible by 7.")
# =============================================================================

# APPROCH 2
# =============================================================================
# num = int(input("Enter a number :"))
# print("The number is divisible by 7.") if num%7==0 else print("The number is not divisible by 7.")
# =============================================================================


#Q.4 Write a program to display "Hello" if a number entered by user is a multiple of five , 
#otherwise print "Bye".

# =============================================================================
# num = int(input("Enter a number :"))
# print("Hello") if num%5==0 else print("Bye")
# =============================================================================


#Q.5 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
# =============================================================================
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# =============================================================================


# =============================================================================
# amt=0
# nu=int(input("Enter number of electric unit : "))
# if nu<=100:
#      amt=0
#      print("Pay :",amt)
# if nu>100 and nu<=200:
#      amt=(nu-100)*5
#      print("Pay :",amt)
# if nu>200:
#      amt= (100*5) +(nu-200)*10
#      print("Amount to pay :",amt)
# =============================================================================


#Q.6 Write a program to display the last digit of a number.
# =============================================================================
# num = int(input("Enter a number : "))
# last = num%10
# print("Last digit of a number :",last)
# =============================================================================


#Q.7 Write a program to check whether the last digit of a number( entered by user ) is 
#divisible by 3 or not.
# =============================================================================
# 
# num = int(input("Enter a number :"))
# last = num%10
# if last%3==0:
#     print("The number is divisible by 3")
# else:
#     print("The number is not divisible by 3.")
# =============================================================================

#Q.8 Write a program to accept percentage from the user and display the grade according to the following criteria:

     #    Marks                                    Grade
      #   > 90                                         A
               #  > 80 and <= 90                       B
               # >= 60 and <= 80                       C
            #below 60                                  D

# =============================================================================
# percentage = float(input("Enter the percentage :"))
# if percentage > 90:
#     print("Grade : A")
# elif percentage > 80 and percentage <= 90:
#     print("Grade : B")
# elif percentage >= 60 and percentage<= 80:
#     print("Grade : C")
# if percentage < 60:
#     print("Grade : D")
# =============================================================================

#Q.9 Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
# =============================================================================
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%
# =============================================================================

# =============================================================================
# price = int(input("Enter the cost of the bike : "))
# road_tax = 0
# if price > 100000:
#     road_tax = (price * 15)/100
#     print("Pay Road Tax : ",road_tax)
# if price < 50000 and price <= 1000000:
#     road_tax = (price*10)/100
#     print("Pay Road Tax : ",road_tax)
# if price <= 50000:
#     road_tax = (price*5)/100
#     print("Pay Road Tax : ",road_tax)
# =============================================================================


#Q.10 Write a program to check whether an years is leap year or not.Write a program to check whether an years is leap year or not.

# =============================================================================
# year = int(input("Enter the year : "))
# if year%100==0:
#     if year%400==0:
#         print("This is a leap year.")
#     else:
#         print("This is not a leap year.")
# else:
#     if year%4==0:
#         print("It is a leap year.")
#     else:
#         print("It is not a leap year.")
# =============================================================================


#Q.11 Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
# =============================================================================
# if num==1:
#     print("Sunday")
# elif num==2:
#     print("Monday")
# elif num==3:
#     print("Tuesday")
# elif num==4:
#    print("Wednesday")
# elif num==5:
#    print("Thursday")
# elif num==6:
#    print("Friday")
# elif num==2:
#    print("Saturday")
# else:
#    print("Please enter number between 1 to 7")
# =============================================================================


#Q.12 Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on

# =============================================================================
# num=int(input("Enter any number between 1 to 12 : "))
# if num==1:
#     print("January : 31days")
# elif num==2:
#     print("February : 28 days")
# elif num==3:
#     print("March : 31days")
# elif num==4:
#     print("April : 30days")
# elif num==5:
#     print("May : 31days")
# elif num==6:
#     print("June : 30days")
# elif num==7:
#     print("July : 31days")
# elif num==8:
#     print("August : 30days")
# elif num==9:
#     print("September : 31days")
# elif num==10:
#     print("October : 30days")
# elif num==11:
#     print("November : 31days")
# elif num==12:
#     print("December : 31days")
# else:
#     print("Please enter number between 1 to 12")
# =============================================================================

#Q.13 Accept any city from the user and display monument of that city.
# =============================================================================
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal
# =============================================================================

# =============================================================================
# print("|--------( Name of Cities )--------|")
# print("1. Delhi\n2. Agra\n3. Jaipur")
# city = input("\nChoose the city : ")
# if city == "Delhi" or city == "1":
#     print("The famous monument of Delhi is Red Fort.")
# if city == "Agra" or city == "2":
#     print("The famous monument in Agra is Taj Mahal.")
# if city == "Jaipur" or city == "3":
#     print("The famous monument of Jaipur is Jal Mahal.")
# =============================================================================


#Q.14 Write a program to check whether a number entered is three digit number or not.
# =============================================================================
# num = input("Enter a number :")
# if len(num)==3:
#     print("It is a 3 digit number.")
# else:
#     print("It is not a 3 digit number.")
# =============================================================================

#Q.15 Write a program to find the lowest number out of two numbers excepted from user.

# =============================================================================
# num1 = int(input("Enter a number for variable a : "))
# num2 = int(input("Enter a number for variable b : "))
# if num1>num2:
#     print(num2,"is the smallest number out of two numbers.")
# if num2>num1:
#     print(num1,"is the smallest number out of two numbers.")
# =============================================================================


#Q.16 Write a program to check whether a number (accepted from user) is positive or negative.
# =============================================================================
# num = int(input("Enter a number : "))
# if num<0:
#     print("It is a negative number.")
# if num>0:
#     print("It is a positive number.")
# =============================================================================

#Q.17 Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
# =============================================================================
# num = int(input("Enter a number : "))
# if num%2==0 and num%3==0:
#     print("The number is divisible by 2 or 3 both.")
# else:
#     print("The number is not divisible by both 2 and 3.")
# =============================================================================

#Q.18 Write a program to check whether a number  is prime or not.
# =============================================================================
# num = int(input("Enter is a number : "))
# k=0
# if num==0 or num==1:
#     k=1
# for i in range(2,num):
#     if num%i==0 :
#         k=1
# if k==1:
#     print("It is a prime number.")
# else:
#     print("It is not a prime number.")
# =============================================================================

#Approch 2
# =============================================================================
# num = int(input("Enter a number : "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("It is not a prime number.")
#             break
#         else:
#             print("It is a prime number.")
# #In case of 0 and 1
# else:
#     print(num,"is not a prime number.")
# =============================================================================



#Q.19 Write a program to check wheather a given character is vowel or not.
# =============================================================================
# vowel = input("Enter a character : ")
# if len(vowel) ==1:
#     pass
# else:
#     print("Error : Please enter a single character first.")
# if vowel == "A" or "a" or "E" or "e" or "I" or "i" or "o" or "O" or "u" or "U":
#     print("It is a vowel.")
# else:
#     print("It is not a vowel.")
# 
# =============================================================================

#Q.20 



num = int(input("Enter a number : "))
if num>1:
    for i in range(2,num):
        if num//i==1:
            print("It is a prime number.")
        else:
            print("It is a prime number.")
        break
#In case of 0 and 1














        