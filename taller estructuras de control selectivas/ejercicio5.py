"""
entradas
ventas del departamento1-->float-->depa1
ventas del departamento2-->float-->depa2
ventas del departamento3-->float-->depa3
salario base-->float-->sb
salidas
venta total-->float-->vt
"""
sb=float(input("Digite el sueldo base:"))
depa1=float(input("Digite el valor de ventas del departamento 1:"))
depa2=float(input("Digite el valor de ventas del departamento2:"))
depa3=float(input("Digite el valor de ventas del departamaneto 3:"))
a=depa1+depa2+depa3
b=(33*a)/100
if(depa1>b):
    print("El salario del departamento 1 es de:"+str(sb+(sb*0.2)))
else:
    print("El salario del departamento 1 es de:"+str(sb))
if(depa2>b):
    print("El salario del departamento 2 es de:"+str(sb+(sb*0.2)))
else:
    print("El salario del departamento 2 es de:"+str(sb))
if(depa3>b):
    print("El salario del departamento 3 es de:"+str(sb+(sb*0.2)))
else:
    print("El salario del departamento 3 es de:"+str(sb+(sb*0.2)))