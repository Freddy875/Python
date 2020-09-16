#Bucle While 

#Este programa pide un numero que sea positivo
#Para calcular su raiz cuadrada 


import math

print("Este programa pide un numero que sea positivo")

print("Para calcular su raiz cuadrada ")

iNumero = int(input("Ingresa un numero: "))

while iNumero < 0:

    print("ERROR. El numero debe ser positivo")

    iNumero = int(input("Ingresa un numero: "))

#fin while

print(f"\nLa raiz cuadrada de tu numero {iNumero} es: {(math.sqrt(iNumero)):.2f}")

#10 Hola Mundo

iContador = 0

while iContador < 10:

    print("Hola Mundo")

    iContador +=1

#Del 0 al 10

iContador = 0

while iContador <= 10:

    print(iContador)

    iContador +=1
