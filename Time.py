from datetime import datetime
from datetime import time

now = datetime.now()
print("Current time is :",now.time())

# Create empty time object

t = time()
print("Time",t)

# Create time object with attribute names
t1 = time(hour=7, minute=10, second=22)
print("Time is :",t1)

t2 = time(7,10,22,5678)
print("Time is :",t2)