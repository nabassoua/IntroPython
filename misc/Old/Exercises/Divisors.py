# Proper divisors of a number

num = int(input("Please enter a positive integer: "))

while num < 1:
    num = int(input("Please enter a positive number: "))

j = 2
div_counter = 0
max_divisor = num/2

print("The proper divisors for", num, "are: ")
while j < max_divisor:
    if num % j == 0:
        print(j, end=" ")
    j += 1

if not div_counter:
        print("\n")
        print(num, "has no proper divisors and is prime")