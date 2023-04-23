#Note :- Big Data concept when we deal with big data. First we take junk of data. First we need to filter it. Then map it after mapping is done. Reduce the mapped data.

# Note :- In this whereever i say function I'm referring a lambda functions.




# First how we create a lambda function

# n = int(input("Enter a number :")) # As you can see first we take a integer.

# a = lambda x: x + x #Then we create a lambda function we give it 'x' as an argument and then give that argument an expression which is x+x. x:x+x here it is necessary if we take x as a argument so we must take x as an expression. After that we pass all this to our function a.

# print(a(n)) #Now function a take argument n as input and act like a function. This n will go to lamda function and then perform operation n+n and store it to n. (i.e x:x+x)



# Now understand the diffrent function we can use with lambda.

# 1. filter() : As it name suggests it takes a list from you and filter that list.


# # Problem Statement : You have a list which have some numbers in it. You have to fetch only even numbers out of it and print all the even numbers.

list1 = [3,2,6,8,4,6,2,9]     # firstly we take a list and put some values on it.
# Now we want to find out the even numbers in the list. 
a = list(filter(lambda x : x%2==0,list1)) #So these are the steps how this works..
# Step 1 : First we create a filter function and pass the list to it.  a = filter(,list1)
# Step 2 : Then because want a list out of it. so we cast it to a list. a = list(filter(,list1))
# Step 3 : Then we pass a lambda function in it.(filter takes 2 arguments 1 is function 2 is iterable(which we want to iterate) in 1 function we pass the condition x: x%2==0 ) So this condition(x:x%2==0) evaluates True. So for according to this condition it will iterate and save values into a
print(a)



# Now we get the even values. If we want to add 2 to each of the values. Whenever we want to access all the elements or want to perform oprations to all the elements.

# 2. map() : When we want to change each value we have to use map().

doubles = list(map(lambda n:n+2,a)) 
#Here lambda have operations which we want to implement it to the each element of the list. map() also takes 2 arguments(1 is function(n:n+2) and 2 is filtered list a.(It can be a normal list))
print(doubles)

# 3. reduce() :In reduce we reduce our mapped list.
from functools import reduce # reduce is not a build-in function with python we have to import it from functools

sum = reduce(lambda a,b : a+b ,doubles) #Here reduce also take 2 arguments(1 is function operation, 2 is iterables). We don't cast into a list because we need a single output. so here what lambda function is doing. We give 2 arguments to lambda  lambda simply add those values.
# For better understanding you can take this function.
# Example : def sum(a,b):
#               return a+b
print(sum)




