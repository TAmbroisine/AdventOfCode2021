import csv


def parse(data: str):
    val_rest = [l for l in data.splitlines()]
    return val_rest


def filtrageSup(i, liste):
    mb0 = 0
    mb1 = 0
    ValeurRestante2 = []
    for ligne in liste:
        if int(ligne[i]) == 1:
            mb1 += 1
        else:
            mb0 += 1
    if mb0 > mb1:
        print("0 est domintant")
        for ligne in liste:
            if int(ligne[i]) == 0:
                ValeurRestante2.append(ligne)
    else:
        print("1 est domintant")
        for ligne in liste:
            if int(ligne[i]) == 1:
                ValeurRestante2.append(ligne)
    return ValeurRestante2


def filtrageInf(i, liste):
    mb0 = 0
    mb1 = 0
    ValeurRestante2 = []
    for ligne in liste:
        if int(ligne[i]) == 1:
            mb1 += 1
        else:
            mb0 += 1
    if mb0 > mb1:
        print("0 est domintant")
        for ligne in liste:
            if int(ligne[i]) == 1:
                ValeurRestante2.append(ligne)
    else:
        print("1 est domintant")
        for ligne in liste:
            if int(ligne[i]) == 0:
                ValeurRestante2.append(ligne)
    return ValeurRestante2


ValeurRestante = []
CO2 = 1
O2 = 1

with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay3.txt') as Input:
    reader = Input.read()
    ValeurRestante = parse(reader)
print(ValeurRestante)
lense = len(ValeurRestante[0])
for i in range(lense):
    print("Indice: " + str(5 - i))
    if len(ValeurRestante) != 1:
        ValeurRestante = filtrageSup(i, ValeurRestante)
    print(ValeurRestante)
O2 = str(ValeurRestante[0])
O2 = int(O2, 2)
ValeurRestante = parse(reader)
for i in range(lense):
    print("Indice: " + str(4 - i))
    if len(ValeurRestante) != 1:
        ValeurRestante = filtrageInf(i, ValeurRestante)
    print(ValeurRestante)
CO2 = str(ValeurRestante[0])
CO2 = int(CO2, 2)
print("O2= " + str(O2) + " et CO2= " + str(CO2))
print("Résultat finale: " + str(O2 * CO2))


"""
def lectureListe(liste):
    for ligne in liste:
        # conversion de la ligne en chiffre
        conv_ligne=int(ligne)
        #calcul la longuer de la ligne
        poids=len(ligne)
        for i in range(poids,-1,-1):
            conv_ligne=decomposition(i,conv_ligne,bit)
    return poids
#détermine si le bit de poids N est égale à 1
def decomposition(poidsBit,chiffre,compteur):
    X=poidsBit
    Y=-poidsBit-1
    if chiffre>=10**poidsBit:
        compteur[Y]=compteur[Y]+1
        chiffre=chiffre - 10**poidsBit
    else:
        compteur[X]=compteur[X]+1
    return chiffre

#Détermine quelle valeur est majoritaire pour un bit donné
def AttributionValeurMajortitaire(compteur):
    X=0
    Y=-0-1
    print(compteur)
    print("X = "+ str(compteur[X]))
    print("Y = "+ str(compteur[Y]))
    if compteur[X]>compteur[Y]:
        print("bit dominant = 1")
        return 1

        for ligne in ValeurRestante:
            # conversion de la ligne en chiffre
            conv_ligne=int(ligne)
            print("le poids est " + str(10**poidsBit))
            if conv_ligne < 10**poidsBit:
                ValeurRestante.remove(ligne)
                print(str(conv_ligne)+" est suprimmée")

    else:
        print("bit dominant = 0")
        return 0

        for ligne in ValeurRestante:
            # conversion de la ligne en chiffre
            conv_ligne=int(ligne)
            if conv_ligne >= 10**poidsBit:
                ValeurRestante.remove(ligne)
                print(str(conv_ligne)+"est suprimmée")


def AttributionValeurCO2(poidsBit,compteur):
    X=poidsBit
    Y=-poidsBit-1
    if compteur[Y]<compteur[X]:
        for ligne in ValeurRestante2:
            # conversion de la ligne en chiffre
            conv_ligne=int(ligne)
            if conv_ligne >= 10**poidsBit:
                ValeurRestante2.remove(ligne)
    else:
        for ligne in ValeurRestante2:
            # conversion de la ligne en chiffre
            conv_ligne=int(ligne)
            if conv_ligne < 10**poidsBit:
                ValeurRestante2.remove(ligne)
    print(ValeurRestante2)

def Departagement():
    conv_ligne=int(ligne)
    if conv_ligne == 0:
        ValeurRestante.remove(ligne)



bit=[0]*26
resultat=[0,0]
ValeurRestante=[]
ValeurRestante2=[]
CO2=1
O2=1

with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay3.txt') as Input:
    reader = Input.read()
    ValeurRestante=parse(reader)
print(ValeurRestante)
poids=lectureListe(ValeurRestante)
BitMaj=AttributionValeurMajortitaire(bit)
if BitMaj==1:
    for ligne in ValeurRestante:
        print("ligne = " + ligne)
        if ligne[0]==0:
            ValeurRestante.remove(ligne)
else:
    for ligne in ValeurRestante:
        if ligne[0]==1:
            ValeurRestante.remove(ligne)
print(ValeurRestante)



for i in range(poids-1,-1,-1):
    #BitMaj=AttributionValeurMajortitaire(i,bit)

    BitMaj=1
    if BitMaj==1:
        for ligne in ValeurRestante:
            conv_ligne=int(ligne)
            print("ligne = " + ligne)
            if ligne(i)==1:
                ValeurRestante.append(ligne)
    else:
        for ligne in ValeurRestante:
            if ligne(i)==1:
                ValeurRestante.append(ligne)
    print(ValeurRestante)

    if len(ValeurRestante)!=1:
        bit=[0]*26
        lectureListe(ValeurRestante)


print("Il reste "+str(len(ValeurRestante))+" valeurs")
print(ValeurRestante)
if len(ValeurRestante)==2:
    Trash=lectureListe(ValeurRestante)
else:
    #O2=int(str(ValeurRestante),2)
    #print("O2 = "+str(O2))
    O2=1

with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay3.txt') as Input:
    reader = csv.reader(Input)
    for ligne in Input:
        ValeurRestante2.append(ligne)
poids=lectureListe(ValeurRestante2)
for i in range(poids-1,-1,-1):
    AttributionValeurCO2(i,bit)
    if len(ValeurRestante2)!=1:
        lectureListe(ValeurRestante2)
if len(ValeurRestante2)==2:
    lectureListe(ValeurRestante2)
else:
    CO2=int(str(ValeurRestante2),2)


print("Life support rating = " + str(CO2*O2))
"""
