# In this exersise we see how the Constructor works in Inheritence 

# class A:

#     def function1(self):
#         print("Function 1 is working.")

#     def function2(self):
#         print("Function 2 is working.")

# class B(A):

#     def function3(self):
#         print("Function 3 is working.")
    
#     def function4(self):
#         print("Functio 4 is working.")


# a = A()

# b = B()

# In above code we simply creating to classes A and B where B inherits the properties of class A.

# Now the first question is "Is constructor running in this code?   => Yes it run internally every time whether you define it or not."

# Ok now we know constructor run every time so let's create a constructor in class A.

# class A:

#     def __init__(self):
#         print("Yo Yo Function.")

#     def function1(self):
#         print("Function 1 is working.")

#     def function2(self):
#         print("Function 2 is working.")

# class B(A):

#     def function3(self):
#         print("Function 3 is working.")
    
#     def function4(self):
#         print("Functio 4 is working.")


# a = A() # It will print "Yo Yo Function."

# b = B() # It will print "Yo Yo Function."

# B also print the constructor of A. What if B have it's own constructor what will happen then..

# Let's see..

# class A:

#     def __init__(self):
#         print("Yo Yo Function.")

#     def function1(self):
#         print("Function 1 is working.")

#     def function2(self):
#         print("Function 2 is working.")

# class B(A):

#     def __init__(self):
#         print("Yo Yo Class B")

#     def function3(self):
#         print("Function 3 is working.")
    
#     def function4(self):
#         print("Functio 4 is working.")

# a = A() # Output : "Yo Yo Function"

# b = B() # Output : "Yo Yo Class B"

# It means first class B checks whether it have his own constructor or not. If not only than it go for constructor of class A.

# Now if we want that b can use it's constructor but as well as it can use constructor of class A.

# For that we have a keyword super()

class A:

    def __init__(self):
        print("Yo Yo Function.")

    def function1(self):
        print("Function 1 is working.")

    def function2(self):
        print("Function 2 is working.")

class B(A):

    def __init__(self):
        super().__init__() # It will execute the constructor of super class(Parent Class)
        print("Yo Yo Class B")

    def function3(self):
        print("Function 3 is working.")
    
    def function4(self):
        print("Functio 4 is working.")

a = A()

b = B()

# As you can see first it execute the class A constructor after that it will go in class B(A) where super() call for constructor of A so it will again execute the constructor of A after that it will execute the constructor of B.

# Output :-
#  
# Yo Yo Function.
# Yo Yo Function.
# Yo Yo Class B



# super() method not only it can call constructor it you can call methods of other class as well.