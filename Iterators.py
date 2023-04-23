# What is an iterator and iterable?
# Iterator is something we can loop over. An iterator has a state where he knows where it is during iteration, Iterator also know how to get their next value they can get next value by using __next__ method. If an object have __iter__ and __next__ method then it is iterable.

# Now the question is how we can say something is iterable ?
# We can know by using dir().we use dir() to know method and attributes available.
# If object have __iter__ method than that object is iterator.

# Let's see..
num = [12,14,15,19]
print(dir(num)) 

# This will print :- ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# As you can see we have an __iter__ method in it. So it is an iterator

# So if we loop over this list.

# num = [12,13,5,16]
# for i in num:
#     print(i)

# So basically what this loop is doing it is calling a method __iter__ and returning an iter that we can loop over. But beacause it doesn't have any __next__ method it means it is not iterable.

# What next method do?
# As we know when we run to loop after each iteration we get a new value. Behind the seen this work is doing by __next__ method.

# Iterator is an object that have countable number of values.
# Let's first create an iterator from a tuple..

# mylist = [12,13,5,16]
# print(next(mylist))

# TypeError: 'list' object is not an iterator

# mytuple = (12,13,15)
# print(next(mytuple))

# TypeError: 'list' object is not an iterator


mytuple = (12,13,15) # Here we create a simple tuple(or you can say object) with three values in it..
iterator = iter(mytuple) # Then here we create an object and make our tuple iterable.
print(next(iterator)) # Output :- 12
print(next(iterator)) # Output :- 13
print(next(iterator)) # Output :- 15
print(next(iterator)) # Output :- StopIteration Exception(It means our iterator has no more values.)

# Here first iterator method makes our tuple iterable then whenever we call next method it print the values inside one by one and because it is iterable it knows where it left so whenever we go for next it knows what already printed so it's goes for next. After this when all the tuple items printed and we try to call next() to get the next value it raise an exeception(StopIteration Exception) which simply means there are no more values in given iterator. This exception is very necessary without this we may be stuck in a infinite loop.



# How to create an iterator in a class?
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object. As we learn __init__ which allows us to do some initialization when the object is created.

# The iter() method acts similar, you can do operations, but must always return the iterator object itself
# The next() method allows you to do operation, and must return the next item in the sequence.


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

# class MyNumbers:

#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# Now we know what will happen if we print by next method. See we never define end of the loop.

# for i in myiter:
#     print(i)

# It goes in an infinite loop



# To prevent the iteration goes forever , we can use StopIteration statement.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# Now it will only print till 20 because this time we are giving StopIteration.
