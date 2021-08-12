"""
Author: Mohamed Nabassoua
Practicing if statements
Exercise: rank 3 inputs from smaller to bigger
"""

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))

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
else:
    print("More work needed....")
