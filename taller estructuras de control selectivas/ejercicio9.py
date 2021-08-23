"""
entradas
nombre-->str-->nombre
monto de la compra-->float-->mc
salidas
monto a pagar-->float-->mp
descuento-->float-->descuento
"""
nombre=str(input("Digite el nombre del cliente:"))
mc=float(input("Digite el monto de la compra:"))

if(mc<50000):
    descuento=0
    mp=(mc*descuento)
    descuento=(mc-mp)

elif(mc<50000 and mc<=100000):
    descuento=0.05
    mp=(mc*descuento)
    descuento=(mc-mp)

elif(mc<100000 and mc<=7000000):
    descuento=0.11
    mp=(mc*descuento)
    descuento=(mc-mp)

elif(mc<700000 and mc<=1500000):
    descuento=1.18
    mp=(mc*descuento)
    descuento=(mc*mp)
elif(mc<1500000):
    descuento=0.25
    mp=(mc*descuento)
    descuento=(mc*mp)

print("Nombre del cliente:"+str(nombre))
print("El monto de la compra es:"+str(mc))
print("El monto a pagar es de:"+str(mp))
print("El descuento es de:"+str(descuento))