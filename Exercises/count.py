# Count the number of data entered by the users

number = int(input("Please enter a positive number: "))
count = 1
total = number

while not (number <= 0):
    number = int(input("Please enter a positive number: "))
    count += 1
    total += number

print("You entered ", count, "numbers", "and their sum is ", total)
