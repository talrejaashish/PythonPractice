# Lesson 1                                                         Class and Object Creation and Calling.

# # Class Creation
# class Computer: # Computer is a Class.

#     def config(self):
#         print("i5,16Gb,1TB")

# # Object Creation
# comp1 = Computer() #com1 is an object.

# # Method 1 to print data in config.
# Computer.config(comp1) # Here first we are calling Computer than calling method(function) and then pass our object to method.

# # Method 2 to print data in config.
# comp1.config() #Here we are using object itself and calling config method. We don't have to mention Computer because when we create comp1 object we already define it.


# # Behind the scene (in comp1.config) .config() takes comp1 as an argument and pass this to method as 'self'(In config function(self)).



# Lesson 2                                                              Special Methods (__methods__)

# class Computer:

#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram

#     def information(self):
#         print("Information is :",self.cpu,self.ram)

# comp1 = Computer('Intel i Core','4GB')
# comp2 = Computer('Intel i5','12GB')

# comp1.information()
# comp2.information()

# We give arguments in comp1 = Computer('Intel i Core','4GB') then this argument goes in __init__(self,cpu,ram). In __init__ method we create cpu and ram variable which will takes comp1 argument as input.(What i mean is cpu = "Intel i Core","4GB"). Then in __init__ method we create self.cpu and self.ram(cpu and ram are just arguments now but we want these argument to be part of our object(Here self is the object) So for connecting them to object we create self.cpu and assaign our cpu argument to it.) 

# self.cpu = cpu is not comulsary you can go for any name.(You can also write it like this : self.fsdh = cpu) but always remember if you go for diffrent name use same name wherever you use it.


# Lesson 3                                                                      Constructor & slef

# class Computer:
#     def __init__(self):
#         self.name = "Abhay"
#         self.age = 21

# c1 = Computer()
# c2 = Computer()

# print(c1.name) # This will print Abhay
# print(c2.name) # This will also print Abhay
# print(c1.age)  # This will print 21
# print(c2.age)  # This will also print 21


# Now if we want to that c2 give us diffrent parameters than c1. We have 2 choices..

# First Choice

# class Computer:
#     def __init__(self):
#         self.name = "Abhay"
#         self.age = 21

# c1 = Computer()
# c2 = Computer()

# c2.name = "Ajay"
# c2.age = 20

# print(c2.name) # This time it will print Ajay
# print(c2.age)  # This time it will print 20


# Second Choice (Use of self)

# class Computer:
#     def __init__(self):
#         self.name = "Abhay"
#         self.age = 21

#     #Second Choice starts from here..
#     def update(self):  # We are creating a function update which will update/change the age of the object
#         self.age = 30  # It will change it to 30. 

# # Now the question is we have 2 objects c1 and c2 with same variable name age. So what will this self.age = 30 do it will change c2.age or it will change c1.age ? Which is the object will update?

# # So here self come into picture. self is like a pointer it will point to the object we want to update. Now the question is how it will point ? 
# # The answer is when we call update() function(method) we are passing object(In this case c1.) into method(like this :- c1.update()). which will go in self. and then update() method do his work and update the value of object.

# c1 = Computer()
# c2 = Computer()

# c1.update() #Here c1 will pass into update as an argument in place of self.

# print(c1.age) #vThis time it will print 30.
# print(c2.age) # It will print 21.



# 
