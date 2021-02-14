#Bulce for

for i in [1,2,3,4,5]:
    print("Hola Mundo")

#fin for

#Itera el valor 5 veces que son los elementos de la lista

#Se puede tener una lista con elementos desodedenados 
#y que no sean numeros y aun asi lo iterara por cada elemento de la lista

print("\n")

for i in [2,10,3,4,"Freddy"]:

    print(f"Elemento: {i}")

#fin for

coleccion = [1,2,3,4,5]


print("\n")

for i in coleccion:
    print("Hola Mundo")

#fin for

#Con un diccionario 

print("\n")

diccionario = {"Freddy":23,"Maria":22,"Jose":45,"Luis":12}

for i in diccionario:
    print(f"{i}")
#fin for


print("\n")

for i in diccionario:
    print(f"{diccionario[i]}")
#fin for


print("\n")

for i in diccionario:
    print(f"{i} : {diccionario[i]}")
#fin for 

print("\n")

for clave,valor in diccionario.items():
    print(f"{clave} : {valor}")
#fin for


print("\n")

#s es por string
sNombre = "Freddy"

for i in sNombre:
    print(f"{i}")
#fin for

print("\n")

for i in sNombre:
    print(f"{i}",end=" ")
#fin for

print("\n")

for i in sNombre:
    print(f"{i}",end=".")
#fin for