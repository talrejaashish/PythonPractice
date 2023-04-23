# MRO = Method Resolution Order

# MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.

#In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.


# Let's understand with example of multiple inheritancee

class A:

    def __init__(self) -> None: # Constructor of A
        print("This is a A class Constructor")

    def feature1(self):
        print("Feature 1 is working.")

    def feature2(self):
        print("Feature 2 is working.")

class B: 

    def __init__(self) -> None: # Constructor of B
        print("This is a B class Constructor")

    def feature3(self):
        print("Feature 3 is working.")

    def feature4(self):
        print("Feature 4 is working.")

class C(A,B): # It means C inherit from B.

    def __init__(self) -> None:
        super().__init__() # What it will execute constructor of A or constructor of B ?
        print("This is a C class constructor.")

    def feature5(self):
        print("Feature 5 is working.")

a = A() # Output :- This is a A class constructor.
b = B() # Output :- This is a B class constructor.
c = C() # Output :- This is a A class constructor. 
                   #This is a B class constructor.

# Now as you can see C(A,B) super.__init__ execute constructor of A. Why?

# Because as we know about operator precedence it goes for left to right according to priority. It's also goes for left to right(no priority) and this what we called MRO.