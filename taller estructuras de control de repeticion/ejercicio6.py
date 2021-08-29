"""
entradas
dividendo-->int-->n1
divisor-->int-->n2
salidas
resto de la division-->int-->restante
"""
n1=int(input("Digite el valor del divisor:"))
n2=int(input("Digite el valor del divisor:"))
while(n1>=n2):
  n1=n1-n2
  restante=n1
  print(n1)