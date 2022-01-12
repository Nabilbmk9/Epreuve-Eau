#Majuscule

import sys


#Gestion d'erreur
if sys.argv[1].isnumeric():
    print("erreur.")
    sys.exit()


#récupérer les variable
argument_to_list = sys.argv[1]

#Fonction
def majuscule():
    liste_arg = []
    tour2=0
    liste_final =[]

    #Mettre l'argument en minuscule
    for i in argument_to_list:
        liste_arg.append(i.lower())

    #Mettre 1 majuscule sur 2
    for j in liste_arg:
        if (j == " ") or (j == "\t") or (j == "\n"):
            tour2 = 0
            liste_final.append(j)

        elif tour2==0:
            liste_final.append(j.upper())
            tour2+=1
        
        elif (j == " ") or (j == "\t") or (j == "\n"):
            tour2 = 0
            liste_final.append(j)
         
        else:
            liste_final.append(j)

    #Mise en forme
    for x in liste_final:
        print(x, end="")

#Lancer la fonction
majuscule()