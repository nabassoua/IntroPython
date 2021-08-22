"""
SIMULATION D'UN DE
@AUTHOR: MOHAMED NABASSOUA
"""

from random import randint

choice = int(input("Veuillez choisir 1 nombre enter 1 et 6: "))
max_simu = int(input("Veuillez choisir le nombre de simulation: "))
positif = 0  # le nombre de fois que la face choisie est apparu
counter = 1  # Compteur pour les simulations

while counter <= max_simu:
    rand_face = randint(1, 6)  # la face du de apres chaque simulation
    print(rand_face, end=' ')
    if choice == rand_face:
        positif += 1
    counter += 1
print("\n")
if positif > 0:
    print(choice, "est apparu", positif, "fois")
elif positif == 0:
    print(choice, "n'est pas apparue")
