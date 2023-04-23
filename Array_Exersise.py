#1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.
 
# from array import *

# n = 5
# print("First we take 5 inputs from the user.")
# a = array('i',[]) # created an empty array
# for i in range(n):
#     b = int(input("Enter a number :"))
#     a.append(b)
# print("The array is :",a)

# print("The elements in the array are :",a)
# m = int(input("Enter the last index of the array as far as you want to print values :"))
# for i in range(m+1):
#     print("Index :",i,"Value :",a[i])

#2. Append 11 into an end of the array.

# from array import *
# a = array('i',[2,3,5,6,9])
# a.append(11)
# print(a)

#3. Write a Python program to reverse the order of the items in the array.

# from array import *

# n = array('i',[1,3,5,7,9,2])

# # Approch 1
# print(n[::-1]) #It will reverse the array.

# # Approch 2
# n.reverse()
# print(n)

#4. Write a Python program to get the length in bytes of one array item in the internal representation. 

# from array import *

# n = array('i',[2,4,6,8,1])

# #for knowing the bytes length of an array we use .itemsize() method.

# print('The orignal array is :',n)

# print("The length of an item in array in the form of bytes is :",n.itemsize)


#5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents and also find the size of the memory buffer in bytes.

# from array import *

# n = array('i',[2,3,5,4,9,7,6])

# print("Current memory address and the length in elements of the buffer: ",n.buffer_info())
# print("The size of the memory buffer in bytes is :",n.buffer_info()[1]*n.itemsize)


#6. Write a Python program to get the number of occurrences of a specified element in an array.

# from array import *

# a = array('i',[2,3,4,2,8,9])

# element = 2
# count = 0
# for i in a:
#     if i==element:
#         count+=1

# print("The",element,"occured",count,"times.")


#7. Write a Python program to append items from inerrable to the end of the array.

# from array import *

# a = array('i',[1,3,5,7,9])
# a.extend(a)
# print(a)


#8. Write a Python program to convert an array to an array of machine values and return the bytes representation

# from array import *

# name = "Abhay"
# print("The string is :",name)
# name1 = list(name)
# b = []
# for i in name1:
#     print("ASCII value of",i,"is :",ord(i))
#     b.append(ord(i))
# print(b)

# a = array('b',b)
# s = a.tobytes()
# print(s)


#9. Write a Python program to append items from a specified list.

# from array import *

# list1 = [1,2,4,5,3,5,7,8]

# # Approch 1
# # a = array('i',list1)
# # print(a)


# # Approch 2
# # a = array('i',[])
# # for i in list1:
# #     a.append(i)
# # print(a)

# # Approch 3
# # a = array('i',[])
# # a.fromlist(list1)
# # print(a)

#10. Write a Python program to insert a new item before the second element in an existing array.

# from array import *
# a = array('i',[1,3,5,7,9])
# n = int(input("Enter the number :"))
# print("Insert new value",n,"before 3")
# a.insert(1,11)
# print(a)


#10.1 Write a program to insert a new item in a array. Take position(index) and value from the user as input.

# from array import *
# a = array('i',[1,3,5,7,9])
# print("Array : ",a)
# for i in range(len(a)):
#     print("Postion :",i+1,"Value :",a[i])

# position = int(input("Enter the position where you want to enter the number : "))
# number = int(input("Enter the number : "))
# if position == 1:
#     a.insert(0,number)
# else:
#     a.insert(position-1,number)
# print(a)


#11. Write a Python program to remove a specified item using the index from an array.

# from array import *

# a = array('i',[1,3,5,8,11])
# print("Orgnal array :",a)
# re = int(input("Enter the index number of item you want to remove :"))
# #a.remove(a[re]) # Here we have to pass array and as well as index of number.
# a.pop(re) # Here we only have to pass index number.

# print("New array :",a)


#12.  Write a Python program to remove the first occurrence of a specified element from an array.

# from array import *

# a = array('i',[1,3,5,8,11])
# print("Orgnal array :",a)
# re = int(input("Enter the number of item you want to remove :"))
# a.remove(re)
# print("New array :",a)

#13.  Write a Python program to convert an array to an ordinary list with the same items.

# Approch 1
# from array import *
# a = array('i',[1,2,3,4,5])
# print("This is an array :",a)
# a = list(a)
# print("This is an list :",a)


# Approch 2
# from array import *
# a = array('i',[1,3,5,7,9,11,15])
# print("This is an array :",a)
# b = []
# for i in a:
#     b.append(i)
# print("This is a list :",b)


#14. Write a Python program to find whether a given array of integers contains any duplicate element. Return true if any value appears at least twice in the said array and return false if every element is distinct.

# from array import *
# a = array('i',[1,3,5,7,9,3,11,15])
# b = set(a)
# if len(a) != len(b):
#     print("False")
# else:
#     print("True")

#15. Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are no such elements.

# def find_first_duplicate(nums):
#     num_set = set()
#     no_duplicate = -1

#     for i in range(len(nums)):

#         if nums[i] in num_set: # This logic used if we want to know the first occurence of a value or to find duplicate elements.
#             return nums[i]
#         else:
#             num_set.add(nums[i])

#     return no_duplicate

# print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
# print(find_first_duplicate([1, 2, 3, 4]))
# print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))

#16. Write a Python program to find a pair with highest product from a given array of integers.
# Only for positive values.
# from array import *

# a = array('i',[2,4,6,8,1,2,4])
# max1 = max(a)
# print(max1)
# b = []
# b.append(max1)
# a.remove(max1)
# print(b)
# print(a)
# max2 = max(a)
# b.append(max2)
# print(b)
# print("Pair :",b)
# print("Highest Product :" ,b[0]*b[1])


#17. Write a Python program to create an array contains six integers. Also print all the members of the array.

# from array import *
# a = array('i',[1,2,4,3,5,7,8,9,1])
# for i in a:
#     print(i)

#18. Write a Python program to get an array buffer information.

# from array import *
# a = array('i',[2,4,6,5,3,7,9,8,2])
# print(a.buffer_info())

#19. Write a Python program to get the length of an array.

# from array import *
# a = array('i',[2,3,5,4,8,7,6])
# print(len(a))


#20. Write a Python program to get the array size of types unsigned integer and float.

# from array import array
# a = array("I", (12,25))
# print(a.itemsize) #It will return the size of bits take in memory.
# a = array("f", (12.236,36.36))
# print(a.itemsize) #It will return the size of bits take in memory.


