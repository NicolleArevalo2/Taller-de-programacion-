"""
entradas
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
salidas
valor total-->int-->vt
"""
A=int(input("Digite el valor A:"))
B=int(input("Digite el valor B:"))
C=int(input("Digite el valor C:"))
D=int(input("Digite el valor D:"))
N1=A
N2=B
N3=C
N4=D
if(C>5):
    C=0
    D=0
    B=B+1
elif(C<5):
    C=0
    D=0
elif(C==5):
    D=0
n1=A
n2=B
n3=C
n4=D
print("el valor aproximado es:"+str(n1)+str(n2)+str(n3)+str(n4))