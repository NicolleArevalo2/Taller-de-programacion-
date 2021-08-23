"""
entradas
distancia-->float-->distancia
salidas
valor a pagar-->float-->vp
"""
distancia=float(input("Digite la distancia recorrida:"))

if(distancia<300):
    vp=50000
    print("El valor a pagar es:"+str(vp))
elif((distancia>=300) and(distancia<1000)):
    vp=(((distancia-300)*30000+70000))
    print("El valor a pagar es:"+str(vp))
elif(distancia>1000):
    vp=(((distancia-300)*9000+150000))
    print("El valor a pagar es:"+str(vp))