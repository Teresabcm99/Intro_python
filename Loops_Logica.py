hello= input(str("Cuáles son los días tiene una semana?")).split(",")
dias_sem= {}
dias_sem['dias']=[]
dias_sem['dias'].append(hello)
print(dias_sem['dias'])
#opt=dias_sem['dias'].len()
############P
import random
dias= ["lunes", "martes", "miercoles", "jueves","viernes","sabado","domingo"]
lista_futbo = ["FC Barcelona", "Real Madrid", "Atlético de Madrid", "Real Sociedad", "Real Betis", "Villarreal", "Athletic Club de Bilbao", "Rayo Vallecano", "Osasuna", "Celta de Vigo", "Mallorca", "Girona", "Getafe", "Sevilla", "Cádiz", "Real Valladolid", "RCD Espanyol", "Valencia", "Almeria", "Elche"]
print(random.sample(lista_futbo, 2))
partidos=[]

for dia in dias:
    equipo_local = random.choice(lista_futbo)
    lista_futbo.remove(equipo_local)
    equipo_visitante = random.choice(lista_futbo)
    lista_futbo.append(equipo_local)
    partido = f"{equipo_local} vs. {equipo_visitante}"
    partidos.append((dia, partido))

for partido in partidos:
    print(f"{partido[0]}: {partido[1]}")

#Hemos creado dos loops, 1 que por cada día de la semana genere dos listas equipo local y equipo visitante. Usando random escoge uno de la lista de equipos, luego se borran para evitar repeticiones. Se guardan los días y los equipos en lista partidos, un ultimo loop da el formato de impresión
#print (f") print con formato luego indices para recuperar los elementos de la lista partidos

#################################################
import random
#import os

intro=(int(input("Diga un número: ")))

number=[]
while True:
    hola= random.randint(0,intro)
    number.append(hola)
    if hola== intro:
        break
print(number)



restar= (int(input("Diga otro numero: ")))

for element in range(0, len(number), restar):
   del number[:element:(element+restar)]
print(number)

while True:
    for i in range(0, len(number)):
        I= (i*3) 
        number[i]=I
        number.append(I)
    print(number)


################################################################################
