# Now if we want to compare two objects.

class Computer:
    def __init__(self): # We use __init__ method here because it will automatically executes whenever we call for object.
        self.age = 30
        self.name = "Abhay"

    # This comparison is based on age. 
    def comparison(self,c2): # Here self is an argument and also c2 is argument.(c2 is changable, but self is not replacable) # Here comparison takes two arguments => compare(who to calling, whom to compare)
        if self.age == c2.age: # Here in place of self we pass c1(internally), So computer read it like this =>if  c1.age == c2.age 
            return True
        else:
            return False

#[return True if self.age == c2.age else return False]
    
c1 = Computer() # We created a object.
c2 = Computer() # We created another object.
c1.name = "Parveen"
# Now what if I want to compare c1 with c2. Let's take a senario that we want to print True if c1 = c2 and print false in case they c1 != c2. 

# In OOP we compare objects on their attributes(i.e age,name) so if we take name as a condition to comparision it only checks the attribute name so it's doesn't matter whether age is same or not. It will only take name as parameter for comparison.

# For Comparison we first need to create a function. (We create it def comparison)

if c1.comparison(c2): # c1(Is the first argument) becomes self and pass it to comparison function(method) and c2 becomes c2(In place of c2 you can take any name it is just for relatability).(In def comparsion we pass this as second argument.) At last it is like this "def comparision(self,c2)"
    print("They are same.") # c1 call c2 and c1 comparing himself with c2. 
else:
    print("They are diffrent.")


# Output will be => They are same. Because c1 attribiute age is same as c2 attribute age. both are 30.
print(c1.age)
print(c1.name)

