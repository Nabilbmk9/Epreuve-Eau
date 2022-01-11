#String dans string

import sys


#Gestion d'erreurs
if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print("erreur.")
    sys.exit()

#Variables
argument1 = sys.argv[1]
argument2 = sys.argv[2]


#Fonction
def string_string():
    if argument2 in argument1:
        print(True)
    else:
        print(False)

string_string()