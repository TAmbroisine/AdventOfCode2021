import csv

#détermine si le bit de poids N est égale à 1
def decomposition(poidsBit,chiffre,compteur):
    X=poidsBit
    Y=-poidsBit-1
    if chiffre>=10**poidsBit:
        compteur[X]=compteur[X]+1
        chiffre=chiffre - 10**poidsBit
    else:
        compteur[Y]=compteur[Y]+1
    return chiffre

#Détermine si pour un bit de poids N quelle valeur a le plus été présent entre 1 et 0 et attribue cet valeur à Gamma et l'autre à Epsilon
def AttributionValeur(resultat,poidsBit,compteur):
    X=poidsBit
    Y=-poidsBit-1
    if compteur[Y]<compteur[X]:
        resultat[0]=resultat[0]+10**poidsBit
    else:
        resultat[1]=resultat[1]+10**poidsBit



bit=[0]*26
resultat=[0,0]
ValeurRestante=[0]

with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay3.txt') as Input:
    reader = csv.reader(Input)
    for ligne in Input:
        # conversion de la ligne en chiffre
        conv_ligne=int(ligne)
        #calcul la longuer de la ligne
        poids=len(ligne)
        for i in range(poids,-1,-1):
            conv_ligne=decomposition(i,conv_ligne,bit)    
for i in range(poids-1,-1,-1):   
    AttributionValeur(resultat,i,bit)
G=int(str(resultat[0]),2)
E=int(str(resultat[1]),2)
print("Epsilon = "+str(E))
print("Gamma = "+str(G))
print("Consommation totale = "+ str(E*G))