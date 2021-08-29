"""
entradas
n-->int-->n
k-->int-->k
salidas
valor de k-->int-->vk
"""
n=int(input("Digite el valor de n:"))
k=int(input("Digite el valor de k:"))
while True:
    if(k<n):
        n=n-1
        print(n)
    break
