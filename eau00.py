# Combinaisons de 3 chiffres


#Variable
chiffre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste = []
liste_final = []

# Fonctions
def combi():
    for i in range(0, len(chiffre)-1):
        for j in chiffre:
            for k in chiffre:
                
                if (i!=j and j!=k and i!=k):
                    liste.append([chiffre[i], chiffre[j], chiffre[k]])               

    for l in liste:
        l.sort()
    liste.sort()

    for p in liste:
        if p not in liste_final:
            liste_final.append(p)
    # Affichage du Résulat en ligne, avec virgule
    tour = 0
    for y in liste_final:
        for x in y: 
            print(x, end="")
        
        tour +=1
        if tour == len(liste_final):
            print(".")
        else:  
            print(end=", ")

# Affichage du résultat
combi()
