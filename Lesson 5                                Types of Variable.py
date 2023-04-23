# In OOP there are two types of variable => 1. Instance Variable 2. Class(Static) Variable

# 1. Instance Variable = Instance Variable are those variable which we define inside the __init__ method.

# 2. Class Variable = A Class Variable is a variable which we define under a class or you can say outside the __init__ method.

# In our main memory we have diffrent namespace 1. Class namespace   2. Object/Instance namespace
# 1. Class namespace => It is a place where you store all the class variable.
# 2. Object/Instance => It is a place where we create all the instance variable.
# Namespace => Namespace is an area where you create and store object/variable.

class Car:
    wheels = 4                            # This a class variable.
    def __init__(self):
        self.milage = 10                  # It is an instance variable.
        self.company = "LAMBORGINI"       # It is an instance variable.

c1 = Car()
c2 = Car()

Car.wheels = 5 # This is shared to each object so now wheels = 5 for c1 as well as for c2.

print(c1.company,c1.milage,c1.wheels) # We need to write c1.wheels because we want to print wheels of c1(Object) We can't write simply wheels or Car.wheels\

print(c2.company,c2.milage,c2.wheels)




# Totally it means if we change a class variable it will affect all the objects(afterall if blueprint is modified all the models(objects) are modified.) If we want to change in class variable we need to call class.(i.e Car.wheels = "Any Number")

# In the case of instance variable if you change it for c1 it doesn't affect c2(as well as if we change c2 it doesn't affect c1.) For change in instance variable we have to call the object which we are changing.(i.e. c1.company = "Change") 