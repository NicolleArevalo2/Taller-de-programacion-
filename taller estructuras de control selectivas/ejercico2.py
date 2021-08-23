"""
entradas
salario bruto-->float-->sb
salidas
descuento-->float-->descuento
nuevo salario-->float-->ns
"""
sb=float(input("Digite el sueldo bruto del trabajador:"))
if(sb<900000):
    ns= (sb*0.15)
    print("El nuevo salario es:"+str(ns))
elif(sb>900000):
    ns=(sb*0.12)
    print("El nuevo salario es:"+str(ns))

