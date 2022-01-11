#Suite de Fibonacci

import sys

# Erreur si pas d'argument ou si plusieur argument ou si pas un chiffre
if (len(sys.argv) < 2) or (len(sys.argv) > 2) or (not sys.argv[1].isnumeric()):
    print("erreur.")
    sys.exit()

#Variable
argument = sys.argv[1]
result = [0, 1]

#Fonction
def fibonacci(x=argument):
    for i in range(0, int(argument)):
        result.append(result[i]+result[i+1])
    print(result[int(argument)])

#Afficher le resultat
fibonacci()