# Methods are the behaviour for an object or for a class.

# We have 3 types of methods : 1. Instance      2. Class        3. Static

# NOTE : In variables Class and Instance are same but in case of methods they are diffrent.

# 1. Instance method have 2 diffrent types : (a) Accessor Methods       (b) Mutator Methods

# (a) Accesor Methods : If you just want to fetch/access the variable of an object you use Accessor Methods.


# (b) Mutator Methods : If you want to modify the variable of an object you have to use Mutator Method.


# # 1. Instance Methods : An instance method is a method that belongs to instances of a class, not to the class itself.

# class Student:

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     # Now if we want to calculate the average of student marks. We simply create a function for it.

#     def average(self):
#         return (self.m1+self.m2+self.m3)/3

#     #(a) Accessor method (Here we just access the m1)
#     def get_m1(self):
#         return self.m1
    

#     #(b) Mutator method (Here we actually can modify the value.)
#     def set_m1(self,value):
#         self.value = value
# a = Student(35,90,85)
# b = Student(45,45,45)

# # and now we print the average

# print(a.average())
# print(b.average())



# 2. Class methods

# class Student:

#     school = "Abhay Classroom" # This is an class variable and we want to work with this variable we have to need some class methods.

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     # Now if we want to calculate the average of student marks. We simply create a function for it.

#     def average(self):
#         return (self.m1+self.m2+self.m3)/3

#     @classmethod
#     def info(cls): # Here we don't use self we use cls because when you work with instance variable we use self but when we work with class variable we use cls.
#         return cls.school


# a = Student(35,90,85)
# b = Student(45,45,45)

# # and now we print the average

# print(a.average())
# print(b.average())

# # Now we print our info method

# #print(s1.info()) #Error it says s1 is not defined. Because info is not in __init__  method. It is a seperate function(method) It is not specific for one object it should work for all the objects. (__init__ print everytime we call an object but that's not the case here.) 

# print(Student.info()) #But it doesn't work so we use a decorator at the top of our info function(method.) After this there will be no error it will print the School Name.

# # Always remember whenever you create a class method use decorators.(Noramally)

# #print(Student.info(cls)) # As you can see it's also get us error because cls is not defined here either.



# 3. Static Method : We use a static method when we want to create a variable which have nothing to do with class variable and nothing to do with instance variable.

class Student:

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    # Now if we want to calculate the average of student marks. We simply create a function for it.

    def average(self):
        return (self.m1+self.m2+self.m3)/3

    #(a) Accessor method (Here we just access the m1)
    def get_m1(self):
        return self.m1
    

    #(b) Mutator method (Here we actually can modify the value.)
    def set_m1(self,value):
        self.value = value

# Static method 
    @staticmethod
    def info(): # We don't pass any argument because it doesn't have(nor class nor instance)
        print("This is a static method")

a = Student(35,90,85)
b = Student(45,45,45)

#print(Student.info()) # This will print none (because def info doesn't have a return value.)


Student.info() # Output : "This is a static method."
print(a.average()) # Output : 70.0
print(b.average()) # Output : 45.0


