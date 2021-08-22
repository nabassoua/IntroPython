# -*- coding: latin-1 -*-


"""
Programme qui propose de deviner un nombre
"""

from random import randint

#on demande les bornes de recherche
val_min = input('Donnez une valeur minimale :')
val_max = input('Donnez une valeur maximale :')
#on choisit une valeur al�atoire dans les bornes indiqu�es
nb_a_trouver = randint(val_min, val_max)
#on initialise la r�ponse de l'utilisateur a une valeur n�cessairement perdante
proposition = val_min - 1

while nb_a_trouver != proposition : #tant que l'utilisateur n'a pas trouv�
    #on lui demande de faire une hypoth�se
    proposition = input('Proposez un nombre compris entre %d et %d : '% (val_min, val_max))
    # si la valeur fournie est correct : entier dans le bon intervalle
    if (type(proposition) == int and proposition >= val_min and  proposition <= val_max) : 
        #alors on le guide dans sa recherche
        if nb_a_trouver > proposition :
            print ("Voyez plus grand !")
        elif  nb_a_trouver < proposition :
            print ("C'est trop !")
    else :
            print ("Le nombre que vous proposez n'est pas dans le bon intervalle ou il ne s'agit pas d'un nombre entier")
print ('BRAVO !')
print ('Le nombre �tait bien %d' % (nb_a_trouver))