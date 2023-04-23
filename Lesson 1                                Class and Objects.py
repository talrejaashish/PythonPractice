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



