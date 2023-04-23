# Basic Idea :- As we know we can have variable and methods inside a class. Now can we have class inside a class?  (The class inside a class called Inner Class.)

# class Student:

#     def __init__(self,name,roll_no):
#         self.name = name 
#         self.roll_no = roll_no

#     # Now I want to create an function to show all the data of Student.
#     def show(self):
#         print(self.name,self.roll_no)

# a = Student('Abhay','191340101001')

# # For print the data one approch is this.
# print(a.name)
# print(a.roll_no)

# # Second approch this when I will create an def show() function.
# a.show()


# Now suppose all students have laptops and we want to know about the information about laptop like brand,cpu,ram we can define it in __init__ method but we know it only create init lengthy so we will create a seperate method for it.

# Let's re-write the code..

class Student:

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop() # Here we create Object for Laptop class.

    def show(self):
        print(self.name,self.roll_no)
    
    # Now we create a Laptop class inside a class
    class Laptop: # We are creating a Inner class for Student class.

        def __init__(self):
            self.brand = "DELL"
            self.cpu = "Raizen"
            self.ram = 8
        # Now the question arise where to create object for laptop class? So we create object for Laptop outside of the Laptop class.
        
a = Student('Abhay', 191340101001)
b = Student('Himanshu',191340101016)
a.show()

# Now if you want to call Laptop class any attributes . 

# Method 1
# print(a.lap.brand)# Here we access brand attribute of laptop. We say 'a.lap.brand'. Here we use 'a' because the laptop object is created inside Student object.

# Method 2 

lap1 = a.lap # Here we create object for lap
lap2 = b.lap # Here we create object for lap

print(lap1.brand) # This will print DELL
print(lap2.cpu)   # This will print Raizen

lap1 = Student.Laptop() # Before calling Laptop we have to call student because Laptop is the inner class of Student class.




# NOTE :- You can create object of inner class inside the outer class or "You can create object of inner class outside the outer class provided you use outer name class to call it."

   