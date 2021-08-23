"""
entradas
piezas-->int-->p
cantidad a pagar po piezas-->float-->c
salidas
valor-->float-->v
inversion-->float-->i
prestamo bancario-->float-->prestamo
credito bancario-->float-->cb
monto a pagara por intereses-->float-->intereses
"""
p=int(input("digite el numero de piezas:"))
c=float(input("Digite el valor de cada pieza:"))
v=(p*c)
if(v<5000000):
    i=(v*0.7)
    cb=(v*0.3)
    intereses=(v*0.2)
    print("el valor que le corresponde pagar a la empresa es:"+str(i))
    print("El valor del credito bancario es:"+str(cb))
    print("El valor del interes es de:"+str(intereses))
else:
    i=(v*0.55)
    prestamo=(v*0.3)
    intereses=(v*0.2)
    cb=(v*0.15)
    print("El valor que le corresponde pagar a la empresa es:"+str(i))
    print("El valor del credito bancario es:"+str(cb))
    print("El valor del interes es de:"+str(intereses))
    print("El valor del prestamo del banco es de:"+str(prestamo))