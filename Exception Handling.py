a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

try:
    # In this block we are saying : Try this code to execute if it is not executed go to except block.
    print(a/b)
except Exception:
    # In this block you will handle it and say what to do if the error occurs.
    print("You can't divide a number by zero.")