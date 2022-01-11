#Paramètres à l’envers

import sys

argument = sys.argv[1:]

for i in argument[::-1]:
    print(i)