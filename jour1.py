
PrevDepth=0
counter=0
###
# incrément A,B,C,D
A=0
B=0
C=0
D=0
#
###
X=0
DepthA=0
DepthB=0
DepthC=0
DepthD=0
"""
Partie1
with open('/home/tam/Bureau/apprentissage/Advent of code/InputDay1.txt') as Input:
    for ligne in Input:
        Depth=int(ligne)
        #Comparaison de la profondeur n avec la profondeur n-1
        if Depth>PrevDepth and X>0:
            counter=counter+1
        PrevDepth=Depth
        X=1
"""

###Partie 2
with open('/home/tam/Bureau/apprentissage/Advent Of Code 2021/InputDay1.txt') as Input:
    for ligne in Input:
        #Somme de la profondeur A
        if A>-1 and A<3:
            DepthA=DepthA+int(ligne)
        #comparaison des profondeurs D et A
        #immédiatement à la fin du calcul de la somme A
        if A==2:
            #repositionnement de l'incrément A
            A=-2
            #Compairaison éxecuté à partir de la seconde somme de A
            if X==1:
                if DepthA>DepthD:
                    counter=counter+1
                DepthD=0
            X=1
        #Somme de la profondeur B
        if B>0 and B<4:
            DepthB=DepthB+int(ligne)
        #comparaison des profondeurs A et B
        #immédiatement à la fin du calcul de la somme B
        if B==3:
            #repositionnement de l'incrément B
            B=-1
            if DepthB>DepthA:
                counter=counter+1
            DepthA=0
        #Somme de la profondeur C
        if C>1 and C<5:            
            DepthC=DepthC+int(ligne)
        #comparaison des profondeurs B et C
        #immédiatement à la fin du calcul de la somme C
        if C==4:
            #repositionnement de l'incrément C
            C=0
            if DepthC>DepthB:
                counter=counter+1
            DepthB=0 
        #Somme de la profondeur D
        if D>2 and D<6:            
            DepthD=DepthD+int(ligne)
        #comparaison des profondeurs C et D
        #immédiatement à la fin du calcul de la somme D   
        if D==5:
            #repositionnement de l'incrément D
            D=1
            if DepthD>DepthC:
                counter=counter+1
            DepthC=0
        A=A+1
        B=B+1
        C=C+1
        D=D+1
#Affichage du résultat
print(counter)

        


