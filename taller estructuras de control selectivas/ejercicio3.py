"""
entradas
A-->int-->A
B-->int-->B
C-->int-->c
D-->int-->D
salidas
expresion1-->float-->expresion1
expresion2-->float-->expresion2
"""
A=int(input("Digite el valor A:"))
B=int(input("Digite el valor B:"))
C=int(input("Digite el valor C:"))
D=int(input("Digite el valor D:"))
if(D==0):
    expresion1=(A-C)**2
    print("El resultado es:"+str(expresion1))
elif(D>0):
    expresion2=((A-B)**3)/D
    print("El valor es:"+str(expresion2))
