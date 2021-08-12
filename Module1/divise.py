"""
Author: Mohamed Nabassoua
Practicing if statements
Exercise: determine if a divides b or b divides a
"""

a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))

if (a % b == 0) or (b % a == 0):
    print("Oui")
else:
    print("Non")
