"""
entrada
diferencia de la lectura anterior-->float-->difl
diferencia de la lecura actual-->float-->da
salida
total de factura-->float-->total
"""
difl=float(input("Digite el valor de la lectura anterior:"))
da=float(input("Digite el valor de la lectura actual:"))
co=difl-da
if(co<=100):
    total=(co*4600)
elif(co>=101 and co<=300):
    total=(co*80000)
elif(co>=301 and co<=500):
    total=(co*100000) 
elif(co>=501):
    total=(co*120000)

print("El monto a pagar es:"+str(total))