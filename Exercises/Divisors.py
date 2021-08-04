# Proper divisors of a number

num = int(input("Please enter a positive integer: "))
j = 2

print("The proper divisors for", num, "are: ")
while j < num:
    if num % j == 0:
        print(j, end=" ")
        j += 1
    else:
        j += 1

else:
    if not (num % 2 == 0):
        print("\n")
        print(num, "has no proper divisors and is prime")