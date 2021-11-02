# Basic iterations in python

# Break statement
# Stops at 4

for x in range(1, 11):
    if x == 5:
        break
    print(x, end=" ")

# 1 2 3 4

print('\n')

# Continue statement
# Skips the number 5

for x in range(1, 11):
    if x == 5:
        continue
    print(x, end=" ")

# 1 2 3 4 6 7 8 9 10

# While-else statement
# "else" is executed only when "while" is done and nothing of substance happens in it
# In other words the "brake" statement in the "while" is not executed

print("\n")

y = int(input("Entrez un entier positif : "))
while not(y > 0):
    y = int(input("Entrez un entier positif, S.V.P. : "))

x = y // 2
while x > 1:
    if y % x == 0:
        print(x, "a pour facteur", y)
        break  # Interruption happens here
    x -= 1
else:
    print(y, "est premier.")

# for-else statement
# "else" is executed only when "for" is done and nothing of substance happens in it
# In other words the "brake" statement in the "for" is not executed

entiers = [2, 11, 8, 7, 5]
cible = int(input("Entrez un entier : "))

for entier in entiers:
    if cible == entier:
        print(cible, "est dans las sequence", entiers)
        break
else:
    print(cible, "n'est pas dans la sequence")
