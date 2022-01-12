#Majuscule sur deux

import sys


#Gestion d'erreur
if sys.argv[1].isnumeric():
    print("erreur.")
    sys.exit()


#récupérer les variable
argument_to_list = sys.argv[1:]

#Fonction
def majuscule_sur_deux():
    liste_arg = []
    tour=0
    tour2=1
    liste_final =[]

    #Mettre l'argument en minuscule
    for i in argument_to_list[tour].lower():
        liste_arg.append(i)
        tour+=1

    #Mettre 1 majuscule sur 2
    for j in liste_arg:
        if j.isalpha():
            tour2+=1
        if tour2%2 == 0:
            liste_final.append(j.upper())
        else:
            liste_final.append(j)
    #Mise en forme
    for x in liste_final:
        print(x, end="")

#Lancer la fonction
majuscule_sur_deux()