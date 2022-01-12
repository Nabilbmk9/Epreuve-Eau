#Index wanted

import sys


#Récuperer la variable
argument = sys.argv[1:]

#Récuperer le dernier element en l'enlevant de la variable
elem_rechercher = argument.pop()


#Si il ne trouve pas afficher -1
if not elem_rechercher in argument:
    print("-1")

#Si il trouve afficher l'indice
else:
    for i in argument:
        if i in elem_rechercher:
            print(argument.index(i))