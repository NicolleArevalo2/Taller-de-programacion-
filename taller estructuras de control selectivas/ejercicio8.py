"""
entradas
P-->int-->P
Q-->int-->Q
salidas
expresion-->int-->expre
"""
P=int(input("Digite el valor de P:"))
Q=int(input("Digite el valor de Q:"))
expre=(P**3)+(Q**4)-(2*(P**2))
if(expre<=680):
    print("P y Q satisfacen la expresion")
else:
    print("P y Q no satisfacen la expresion")