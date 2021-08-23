"""
entrada
edad-->int-->edad
nivel de hemoglobina-->float-->nh
sexo-->str-->sexo
salidas
resultado negativo o positivo-->str-->r
"""
edad=int(input("Digite su edad en meses:"))
nh=float(input("Digite el nivel de hemoglobina:"))
sexo=str(input("Digite 1 si es feminina y 2 si es masculino:"))

if(edad>=0 and edad<=1):
    if(nh>=12 and nh<=26):
        r="negativo para anemia"
else:
    if(nh<12):
        r="positivo para anemia"
if(edad>1 and edad<=6):
    if(nh>=10 and nh<=18):
        r="negativo para anemia"
else:
    if(edad<10):
        r="positivo para anemia"
if(edad>6 and edad<=12):
    if(nh>=11 and nh<=15):
        r="negativo para anemia"
else:
    if(nh<11):
        r="positivo para anemia"
if(edad>1 and edad<=10):
    if(nh>=11.5 and nh<=15):
        r="negativo para anemia"
else:
    if(nh<11.5):
        r="positivo para anemia"
if(edad>5 and edad<=10):
    if(nh>=12.6 and nh<=10):
        r="negativo para anemia"
else:
    if(nh<12.5):
        r="positivo para anemia"
if(edad>10 and edad<=15):
    if(nh>=13 and nh<=15.5):
        r="negativo para anemia"
else:
    if(nh<13):
        r="positivo para anemia"
if(edad>15):
    if(nh>=12 and nh<=16):
        r="mujer negativo para anemia"
else:
    if(nh<12):
        r="mujer positivo para anemia"
if(edad>15):
    r="hombre negativo para anemia"
else:
    if(nh<15):
        r="hombre positivo para anemia"    
print("El resultado es:"+str(r))