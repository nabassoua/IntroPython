"""
Author: Mohamed Nabassoua
Topic: Functions
Task: Returns the maximum among a list of 3 numbers
"""


def cherche_max_triplet(a, b, c):
    """
    Fonction qui étant donnés trois nombres a, b, c retourne le maximum
    a : float
    b : float
    c : float
    -> float
    """
    maxi = a
    if b > maxi:
        maxi = b
        if c > maxi:
            maxi = c
    else:
        if c > maxi:
            maxi = c
    return maxi

#######################################
# Programme principal
#######################################


a, b, c = input('Entrez trois nombres séparés par une virgule : \n').split(",")
max1 = cherche_max_triplet(a, b, c)
print(max1)
a, b, c = input('Entrez à nouveau trois nombres séparés par une virgule : \n').split(",")
max2 = cherche_max_triplet(a, b, c)
print(max2)
a, b, c = input('Entrez enfin trois nombres séparés par une virgule : \n').split(",")
max3 = cherche_max_triplet(a, b, c)
print(max3)
maximum = cherche_max_triplet(max1, max2, max3)
print(maximum)
