"""
Author: Mohamed Nabassoua
Practicing if statements
Exercise: rank 3 inputs from smaller to bigger
"""

a = input("Please enter the first number: ")
b = input("Please enter the second number: ")
c = input("Please enter the third number: ")

# Need to check if the user entered numbers...
if ((type(a) != int and type(a) != float) or (type(b) != int and type(b) != float) or (type(c) != int and type(c) != float)):
    print("Try again, please enter numbers")
else:
    if a <= b and b <= c:
        print(a, b, c)
    elif b <= a and a <= c:
        print(b, a, c)
    elif c <= a and a <= b:
        print(c, a, b)
    elif c <= b and b <= a:
        print(c, b, a)
    elif a <= c and c <= b:
        print(a, c, b)
    elif b <= c and c <= a:
        print(b, c, a)

