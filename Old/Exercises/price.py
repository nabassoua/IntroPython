# Compute the price of an item

price = int(input("Please enter the price: "))

while price > 0:
       print("The total price is: ", ((1.5/100) * price) + price)
       price = int(input("Please enter the price: "))

print("Bye!")