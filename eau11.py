#Différence minimum absolue
import sys

#Gestion d'erreur
if (len(sys.argv) < 3) :
    print("erreur.")
    sys.exit()

for i in sys.argv[1:]:
    if i.isalpha():
        print("erreur.")
        sys.exit()

#Recupere la variable
argument = sys.argv[1:]
argument2=[]
for i in argument:
    argument2.append(int(i))
argument2.sort(reverse=True)

#Fonction
def min_absolue():
    difference = []
    tour=0
    for i in argument2[0:-1]:
        difference.append(int(i)-int(argument2[int(tour)+1]))
        tour +=1
    difference.sort()
    print(difference[0])

min_absolue()