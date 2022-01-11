#Combinaisons de 2 nombres

chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste = []
liste2 = []
liste3 = []
tour = 0

#Créer une liste 
for a in chiffre:
    for b in chiffre:
        liste.append([str(a) + str(b)])

for c in range(len(liste)):
    for d in range(len(liste)):
        if liste[c] != liste[d] :
            liste2.append(liste[c] + liste[d])
            
for e in range(len(liste2)):
    liste2[e].sort()
    if liste2[e] not in liste3:
        liste3.append(' '.join(liste2[e]))
        

for f in liste3:
    for g in f:
        print(g, end="")
    tour +=1
    if tour == len(liste3):
        print(".")
    else:  
        print(end=", ")

