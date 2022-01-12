#Par ordre Ascii

import sys


#Fonction
def tri_ordre_ascii(argument=sys.argv[1:]):

    ordre_ascii = ['!','"', '#','$','%','&',"'",'(',')',
'*','+',',','-','.','/','A', 'B', 'C', 'D', 'E','F',
'G','H','I','J','K','L','M','O','P','Q','R','S','T',
'U','V','W','X','Y','Z','a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z','{','|','}','~']

    permutation = True

    while permutation:
        permutation=False
        for i in range(0, len(argument)-1):

            #Faire le tri en comparant au tableau ascii 
            if ordre_ascii.index(argument[i][0]) > (ordre_ascii.index(argument[i+1][0])):
                argument[i], argument[i+1] = argument[i+1], argument[i]
                permutation=True
    
    #Affiche
    for j in argument:
        print(j, end=" ")
    return
        
tri_ordre_ascii()
