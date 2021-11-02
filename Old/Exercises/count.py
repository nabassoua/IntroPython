# Count the number of data entered by the users

number = int(input("Please enter a positive number: "))
count = 0
total = 0
hund_count = 0

while number > 0:
    total += number
    count += 1
    if number > 100:
        hund_count += 1
    number = int(input("Please enter a positive number: "))

print("You entered ", count, "numbers,", "and their sum is ", total, ".", "And there are", hund_count, "bigger than 100.")
