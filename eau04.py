#Prochain nombre premier

import sys


#Gestion erreurs
if (len(sys.argv) < 2) or (len(sys.argv) > 2) or (not sys.argv[1].isnumeric()):
    print("-1")
    sys.exit()

# Variable
argument = sys.argv[1]
stop = False
tour = 1

# Fonction
while stop == False:
    stop = True
    argument = int(argument)+1
    for i in range(2, argument):
        if argument%i == 0:
            stop = False

print(argument)    

   
             
