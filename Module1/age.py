#!/bin/env python
# -*- coding: utf-8 -*-
"""Jeu d'age"""
# fichier : age.py
# auteur: Mohamed Nabassoua

import random

def tester_age(age):
    if age < 10:
        print("Vous êtes un enfant")
    elif age >= 10 and age <= 17:
        print("Vous êtes un adolescent")
    elif age >= 18 and age <= 49:
        print("Vous êtes un adulte")
    else:
        print("Vous êtes un vétéran")


#######################################
# Programme principal
#######################################

my_age = random.randint(1, 100)
print("Your random age is:", my_age, end=' ')
print("\n")
tester_age(my_age)