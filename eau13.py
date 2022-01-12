#Tri par sélection

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
def tri_par_selection(liste=sys.argv[1:]):
    for i in range(len(liste)):
      # Trouver le min
       tour = i
       for j in range(i+1, len(liste)):
           if liste[tour] > liste[j]:
               tour = j
       
       liste[i], liste[tour] = liste[tour], liste[i]

    #Affichage
    for h in liste:
        print(h, end=" ")


tri_par_selection()