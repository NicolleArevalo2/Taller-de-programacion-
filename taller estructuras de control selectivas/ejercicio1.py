"""
entrada
cantidad invertida-->float-->c
tasa de intereses-->float-->t
salida
intereses-->float-->i
ganancia total-->float-->total
"""
c=float(input("Escriba la cantidad invertida:"))
t=float(input("Escriba la tasa de interes:"))
i=(c*t)/100
if (i>100.000):
    print("Los intereses son:"+str(i))
total=c + t
print("el salario total es:"+str(total))