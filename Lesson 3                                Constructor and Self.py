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

class Computer:
    def __init__(self): # Init is also a constructor
        self.name = "Abhay"
        self.age = 21

    #Second Choice starts from here..
    def update(self):  # We are creating a function update which will update/change the age of the object
        self.age = 30  # It will change it to 30. 

# Now the question is we have 2 objects c1 and c2 with same variable name age. So what will this self.age = 30 do it will change c2.age or it will change c1.age ? Which is the object will update?

# So here self come into picture. self is like a pointer it will point to the object we want to update. Now the question is how it will point ? 
# The answer is when we call update() function(method) we are passing object(In this case c1.) into method(like this :- c1.update()). which will go in self. and then update() method do his work and update the value of object.

c1 = Computer()
c2 = Computer()

c1.update() #Here c1 will pass into update as an argument in place of self.

print(c1.age) #vThis time it will print 30.
print(c2.age) # It will print 21.


