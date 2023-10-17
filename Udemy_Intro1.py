print("Hello World")
message= "Hello World"
#N_of_Apple = 5
#print(N_of_Apple)

#if N_of_Apple > 5:
  #  N_of_Apple == 5
   # print(True)
#else:
    #print(False)

# Tipos de variable repaso
name = "Valdemoro"
#print(type(name))
#print(type(N_of_Apple))
#print(type(name))
degree = 95.6
print(type(degree))
# Los decimales son Float en PY

# Attempt



values = [1, 0, 1, 0, 1, 1, 0]

is_raining = 1
is_sunny = 0
for element in (values):
    if element ==1:
        print("is_raining")
    else:
        print("is_sunny")


macarrones= 24
print(float(macarrones))

#Rememeber concat

print("Hello"+ " "+"Martha"+"!")
#Only works for strings, remember to add spaces/or transform data types

#Indexr en statement name[2] o name [-2] cuenta caracteres delante o detrás si -

print(name.find("d")) #otra forma, es counter de characters, si está repetido solo sale el 1 . También palabras

print(message.replace("Hello", "Bye"))

#Formatos
message.lower()
message.upper()
message.capitalize()

#Aritmética + - * / y % resto divisón)
#round(n, decimal) also abs() (valor absoluto) pow(n,n potencia)

#If statements
#If 1 condicion
#Elif 2 condción si 1 condición falla
#Else si ninguna de las 2 cond es True

#If se sujeta según com booleans o True o False

#If con más de una condición a la vez
# if and (las dos condiciones tienen que ser true

hungry=True
thirsty=True

if hungry and thirsty:
    print("Go eat smthing.")
#Si solo queremos que una de las dos condiciones se True se usa or
if hungry or thirsty:
    print("Go eat")

#Si queremos que una de las condiciones  se usa not (Que una sea verdadera)
if hungry and not thristy:
    print("Eat burger")

#Comparison operator #using if
#Averigua si el num es positivo, negativo o 0

num=6
if num>0:
    print("num is positive.")
elif num<0:
    print("num is negative.")
else
    print("num is 0.")

    #Operator > < >= <= == !=(unequal to)


#While until certain condition is met # something has to change variable, otherwise always true

i=10
while i >=20:
    print("Funciona")
    i=i+1
print("Finish")

#list entre [,] va con strings, numeros etc.. se pueden mezclar dif tipos de datos
# [:] dar valores de lista entre (el último no seu cuenta)
#.append mete datos | .clear borrar | .count (elementos repetidos en lista) | .index (1st appeareance in list)
#.insert (n, objeto) mete objeto en indice | .reverse revierte el orden de la lista| .sort ordena alfabeticamente
#.copy

#For puede or recorrer toda la lista o un rango| for i in range() 1, 2 (rango) , 5 (by)

#Nested loops y listas (como poner cosas dentro de los loops y listas) macarrones [filas] [columna]
#tuplas es una "lista sin paréntesis no modificable" para datos no moldificables. len si se puede usar


#Funciones
#se usaa el prompt def para definir la función -> def say hello():
#pass arguments to a function ->def say_hello(name) se puede poner más de uno, no tienen porque aparecer en la misma línea
#return statement

def add_two_numbers(num1, num2):
    return (num1+num2)

print(add_two_numbers(9,10))