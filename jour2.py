import csv
X=0
Y=0
Z=0
"""
Partie 1
with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay2.txt') as Input:
    reader = csv.reader(Input)
    for ligne in Input:
        #séparation de la direction et de la valeur du changement
        split_ligne=ligne.split()
        if 'forward' in ligne:
            X=X+int(split_ligne[1])
        elif 'up'  in split_ligne[0]:
            Y=Y-int(split_ligne[1])
        elif 'down'  in split_ligne[0]:
            Y=Y+int(split_ligne[1])
    print('position horizontale: '+ str(X))
    print('profondeur: '+ str(Y))
    print ('position finale: '+ str(Y*X))
"""

#Partie 2
with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay2.txt') as Input:
    reader = csv.reader(Input)
    for ligne in Input:
        #séparation de la direction et de la valeur du changement
        split_ligne=ligne.split()
        if 'forward' in ligne:
            X=X+int(split_ligne[1])
            Y=Y+Z*int(split_ligne[1])
        elif 'up'  in split_ligne[0]:
            Z=Z-int(split_ligne[1])
        elif 'down'  in split_ligne[0]:
            Z=Z+int(split_ligne[1])
    print('position horizontale: '+ str(X))
    print('profondeur: '+ str(Y))
    print ('position finale: '+ str(Y*X))