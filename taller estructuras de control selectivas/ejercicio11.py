"""
Entradas
temperatura-->float-->t
Salidas 
deporte-->float-->d
"""
t=float(input("Digite la temperatura:"))
if(t>85):
    d="natacion"
elif(t>=71 and t<=85):
    d="tennis"
elif(t>32 and t<=70):
    d="glof"
elif(t<10 and t<=32):
    d="esqui"
elif(t<=10):
    d="marcha"
print(d)