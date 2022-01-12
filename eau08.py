#Chiffres only

import sys

#variable a récuprer
argument = sys.argv[1:]

#Fonction
def chiffre_only(argmuent = argument):
    for i in argmuent:
        if not i.isnumeric():
            return print(False)
    return print(True)

chiffre_only()