"""
entradas
a-->int-->a
b-->int-->b
c-->int-->c
d-->int-->d
salidas
x1-->int-->x1
x2-->int-->x2
"""
a=int(input("digite el valor a:"))
b=int(input("digite el valor b:"))
c=int(input("digite el valor c:"))
d=b**2-4*a*c
if(d==0):
    x=(-b/(2*a))
    print("la solucion es:"+str(x))
elif(d>0):
    x1=((-b)+((b**2-(4*a*c))/(2*a))**0.5)
    x2=((-b)-((b**2-(4*a*c))/(2*a))**0.5)
    print("la solucion es:"+str(x1))
    print("la solucion es:"+str(x2))
elif(d<0):
    print("no tiene solucion en los reales:")