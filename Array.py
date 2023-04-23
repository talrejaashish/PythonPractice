#Python doesn't have built-in array we have to import it from module array.

# from array import * # import * means everything.

# #1. Create an empty array.
# arr = array('i',[]) # Here we created empty array 'i' indicates the type of values we store in our array('i' means integer.). So we can only put integer values in it.



#2. How you add values into an array.

# from array import *
# n = int(input("Enter the length of the array :"))
# arr = array('i',[])
# for i in range(n):
#     a = int(input('Enter the value :'))
#     arr.append(a)
# print(arr)


#3. Find an element in the arry

from array import *
n = int(input("Enter the length of the array :"))
arr = array('i',[])
for i in range(n):
    a = int(input('Enter the value :'))
    arr.append(a)
print(arr)

count = 0
m = int(input("Enter a you want to search :"))
# for i in arr:
#     if i == m:
#         print("The value present in the array.")
#         break
#     count+=1
# print("Value",i,"present at",count,"index.")


# Or you can do you can use a method for it.

print(arr.index(m)) # This wil also work same the upper for loop will do.