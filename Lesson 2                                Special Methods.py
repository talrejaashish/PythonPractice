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


