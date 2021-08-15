"""
Author: Mohamed Nabassoua
Exercise: find the number of trials it takes to see a chosen number by the user on the face of a die
"""
import random

num_trials = int(input("Please enter the number of trials: "))
face_number = int(input("Please choose a face number on the die: "))

num_steps = 1  # Trials counter
num_sucess = 0  # Number of trials until sucess
print("The random numbers are:", end=' ')

while num_steps <= num_trials:
    random_face = random.randint(1, 6)  # The computer selects a random face between 1 and 6
    print(random_face, end=' ')
    num_steps += 1
    num_sucess += 1
    if random_face == face_number:
        print("\n")
        print("It took", num_sucess, "Trial(s) to get the number", face_number)
        break

