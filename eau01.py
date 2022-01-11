#Combinaisons de 2 nombres

chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste = []
liste2 = []
liste3 = []
tour = 0

#Créer une liste avec toute les combinaison de 2 chiffres
for a in chiffre:
    for b in chiffre:
        liste.append([str(a) + str(b)])

# Refaire le 1 mais 2 fois en retirant les doublons
for c in range(len(liste)):
    for d in range(len(liste)):
        if liste[c] != liste[d] :
            liste2.append(liste[c] + liste[d])

# Trier le tout et enlever les doublons
for e in range(len(liste2)):
    liste2[e].sort()
    if (liste2[e][0]) + " " + (liste2[e][1]) not in liste3:
        liste3.append(' '.join(liste2[e]))


        
# Print en ligne avec une virgule
for f in liste3:
    for g in f:
        print(g, end="")
    tour +=1
    if tour == len(liste3):
        print(".")
    else:  
        print(end=", ")

