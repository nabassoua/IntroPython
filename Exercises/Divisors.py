# Divisors of a number

num = int(input("Please enter a number: "))

for i in range(1, num):
    if num % i == 0:
       print("divisors= ", i)
       continue
    else:
        continue
else:
    print("The number is prime?")

        