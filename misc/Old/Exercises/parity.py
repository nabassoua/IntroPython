# Returns the parity of a number

num = int(input("Please enter a number: "))

while num < 1:
    num = int(input("Please enter a number: "))

if num % 2 == 0:
    print(num, "is EVEN")
else:
    print(num, "is ODD")