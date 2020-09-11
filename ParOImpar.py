'''
Pedir dos numeros 
y devolver cual es par y cual es impar
o si los dos son impares
'''

iNumero1 = int(input("Ingresa el primer numero (entero): "))

iNumero2 = int(input("Ingresa el segundo numero (entero): "))

if iNumero1%2==0 and iNumero2%2==0:
    print(f"{iNumero1} y {iNumero2} ambos son numeros pares")
elif iNumero1%2==0 and iNumero2%2!=0:
    print(f"{iNumero1} es par y {iNumero2} es impar")
elif iNumero1%2!=0 and iNumero2%2==0:
    print(f"{iNumero1} es impar y {iNumero2} es par")
else:
    print(f"{iNumero1} y {iNumero2} ambos son numeros impares")
#fin if-else