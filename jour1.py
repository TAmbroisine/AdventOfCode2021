
PrevDepth=0
counter=0
A=0
B=0
C=0
D=0
DepthA=0
DepthB=0
DepthC=0
DepthD=0
"""
Partie1
with open('/home/tam/Bureau/apprentissage/Advent of code/InputDay1.txt') as Input:
    for ligne in Input:
        Depth=int(ligne)
        if Depth>PrevDepth and X>0:
            counter=counter+1
        PrevDepth=Depth
        X=X+1
"""   
with open('/home/tam/Bureau/apprentissage/Advent of code/InputDay1.txt') as Input:
    for ligne in Input:
        if A==4:
            A=0
            if DepthB>DepthA:
                counter=counter+1
            DepthA=0
        if A>=0 and A<3:
            
            DepthA=DepthA+int(ligne)
        if B==5:
            B=0
            if DepthC>DepthB:
                counter=counter+1
            DepthB=0
        if B>=1 and B<4:
            
            DepthB=DepthB+int(ligne)
        if C==6:
            C=0
            if DepthD>DepthC:
                counter=counter+1
            DepthC=0
        if C>=2 and C<5:
            
            DepthC=DepthC+int(ligne)
        if D==7:
            D=3
            if DepthA>DepthD:
                counter=counter+1
            DepthD=0
        if D>=0 and D<6:
            
            DepthD=DepthD+int(ligne)
        A=A+1
        B=B+1
        C=C+1
        D=D+1
print(counter)

        


