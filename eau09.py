#Entre min et max

import sys

#Gestion d'erreurs
if (len(sys.argv)< 3) or (len(sys.argv)>3) or not (sys.argv[1].isnumeric()) or not (sys.argv[2].isnumeric()):
    print("erreur.")
    sys.exit()

#Récupère les variable
argument = sys.argv[1:]


#Fonction
def entre_min_et_max(argument=argument):
    argument.sort()
    for i in range(int(argument[0])+1, int(argument[1])):
        print(i, end=" ")

entre_min_et_max()