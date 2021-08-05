# Count the number of times a number is divisible by 2

num = int(input("Please enter a number: "))

while num < 1:
    num = int(input("Please enter a number: "))

count = 0
original_num = num

while num % 2 == 0:
    count += 1
    num = num // 2

print(original_num, "is divisible by 2", count, "times")