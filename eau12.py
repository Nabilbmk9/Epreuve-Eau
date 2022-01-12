#Tri à bulle

import sys


#Gestion d'erreur
if (len(sys.argv) < 3) :
    print("erreur.")
    sys.exit()

for i in sys.argv[1:]:
    if i.isalpha():
        print("erreur.")
        sys.exit()

#Fonction
def tri_a_bulle(liste=sys.argv[1:]):
    permutation = True
    j = 0
    while permutation:
        permutation = False
        j += 1
        for i in range(0, len(liste)-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                permutation = True
    #Affichage
    for h in liste:
        print(h, end=" ")


tri_a_bulle()