# -*- coding: latin-1 -*-
"""
Utilisation de la base de donn�es client_commande acceptant les requ�tes SQL
"""
 
import sqlite3
# import sys


def shema_table(cnx, table):
    """
    Retourne la liste des champs d'une table
    """
    champs = []
    types = []
    nulles = []
    keys = []
    cur = cnx.cursor()
    cur.execute("PRAGMA table_info(%s)" % table)
    for enreg in cur:
        champs.append(enreg[1])
        types.append(enreg[2])
        if enreg[3]:
            nulles.append('(NOT NULL)')
        else:
            nulles.append('')
        if enreg[5]:
            keys.append('PRIMARY KEY ')
        else:
            keys.append('')
    cur.execute("PRAGMA foreign_key_list(%s)" % table)
    for enreg in cur:
        ind = champs.index(str(enreg[4]))
        keys[ind] += 'FOREIGN KEY REFERENCES '+enreg[2]+'.'+enreg[3]
    cur.close()
    return champs, types, nulles, keys


def affiche_schema(cnx):

    print("\n Son sch�ma est le suivant :")
    print("---------------------------")
    cur = cnx.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    for enreg in cur: 	# Affichage du r�sultat
        print(enreg[0])
        champs, types, nulles, keys = shema_table(cnx, enreg[0])
    
        for i in range(len(champs)):
            print('\t', champs[i], '\t: ', types[i], nulles[i], keys[i])
    cur.close()
    # print "---------------------------"


def affiche_select(cur):
    r = cur.fetchone()
    if r:
        print("\nVoici les donn�es extraites de la base de donn�es suite � votre requ�te :\n")
        # on r�cup�re les noms des colonnes
        champs = r.keys()
    
        donnees = []
        for value in r:
            donnees.append([value])
           
        for enreg in cur: 	# Affichage du r�sultat
            for i in range(len(enreg)):
                donnees[i].append(enreg[i])

        lenghts = []
        for liste in donnees:
            temp = []
            for value in liste:
                temp.append(len(str(value)))
            lenghts.append(max(temp))
        
        # affichage des donn�es
        
        ligne = ''
        for i in range(len(champs)):
            ligne += str(champs[i]).center(lenghts[i]+5)
        print(ligne)
        print('-'*len(ligne))
        
        for i in range(len(donnees[0])):
            ligne = ''
            for j in range(len(donnees)):
                ligne += str(donnees[j][i]).center(lenghts[j]+5)
            print(ligne)
    else:
        print("\nIl n'y a pas de donn�es correspondant � votre demande !")
    
# ------------------------------------------------------------------------------
#             Programme principal
# ------------------------------------------------------------------------------
    

basename = "client_commande.sqlite"
print("Vous travaillez sur la base de donn�es", basename.split('.')[0])
print("======================================================")

baseDonn = sqlite3.connect(basename)


affiche_schema(baseDonn)


go_on = 1
while go_on:
    print((""")
         ----------------------------------------------------------    
         Veuillez entrer soit :
         * votre requ�te SQL suivie d'un ';'
         * SCHEMA pour faire r�afficher le sch�ma de la base 
         * ou END pour terminer :
         ----------------------------------------------------------
    """))
    continue_saisie = 1
    requete = ''
    while continue_saisie:
        requete += input()+'\n'
        if ';' in requete or 'END' in requete or 'SCHEMA' in requete:
            continue_saisie = 0
    # print requete
    if 'END' in requete:
        go_on = 0
    elif 'SCHEMA' in requete:
        affiche_schema(baseDonn)
    else:
        try:
            sav = baseDonn.row_factory  # sauvegarde de l'ancienne valeur (None par d�faut)
            baseDonn.row_factory = sqlite3.Row
            cur = baseDonn.cursor()
            baseDonn.row_factory = sav  # retour � l'ancienne valeur
            cur.execute(requete[:-1])	   # ex�cution de la requ�te SQL            
        except sqlite3.Error as e:
            print('\n*** Requ�te SQL incorrecte ***')
            print("Voici l'erreur retourn�e par sqlite :", e.args[0])
        else:
            if 'SELECT'.lower() in requete.lower():
                affiche_select(cur)
            else:
                print("\nVotre requ�te a modifi� le contenu de la table")
                requete_words = requete.split()
                if requete_words[1].lower() == 'INTO'.lower() or requete_words[1].lower() == 'FROM'.lower():
                    table = requete_words[2]
                else:
                    table = requete_words[1]
                choix = raw_input('Voulez-vous afficher le contenu de la table ? (o/*)\n')
                if choix.lower() == "o":
                    requete = 'select * from '+table
                    cur.execute(requete)
                    affiche_select(cur)
                choix = raw_input('\nVoulez-vous valider la modification effectu�e ? (o/*)\n')
                if choix.lower() == "o":
                    baseDonn.commit()
                    print("La base de donn�es a �t� mise � jour.")

                    
choix = input("\n Confirmez-vous l'enregistrement de l'�tat actuel de la base de donn�es (o/*) ? ")
if choix.lower() == "o":
    baseDonn.commit()
    print("\n La base de donn�es a �t� mise � jour.")
else:
    print("\n Les modifications r�alis�es depuis votre derni�re validation sont annul�es.")

baseDonn.close()
print("Au revoir !")

