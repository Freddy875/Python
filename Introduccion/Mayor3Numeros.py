'''
Pedir 3 numeros 
y determinar cual es el mayor 
'''

iNumero1 = int(input("Ingresa el primer valor (entero): "))

iNumero2 = int(input("Ingresa el segundo valor (entero): "))

iNumero3 = int(input("Ingresa el tercer valor (entero): "))

if iNumero1==iNumero2 and iNumero1==iNumero3:
    #Validamos que los tres numeros sean iguales
    print(f"{iNumero1}, {iNumero2} y {iNumero3}",
    "los tres valores son iguales")
elif iNumero1==iNumero2 and iNumero1 > iNumero3:
    #En este caso validamos que el primer y segundo número 
	#sean iguales y que sean mayores al tercero
    print(f"{iNumero1} y {iNumero2}",
    f"son iguales y mayores que {iNumero3}")
elif iNumero1==iNumero3 and iNumero1 > iNumero2:
    #En este caso validamos que el primer y el tercer número 
	#sean iguales y mayores que el segundo
    print(f"{iNumero1} y {iNumero3}",
    f"son iguales y mayores que {iNumero2}")
elif iNumero2==iNumero3 and iNumero2 > iNumero1:
    #En este caso validamos que el segundo y el tercer número
	#sean iguales y mayores que el primero
    print(f"{iNumero2} y {iNumero3}",
    f"son iguales y mayores que {iNumero1}")
elif iNumero1 > iNumero2 and iNumero1 > iNumero3:
    #A partir de este punto ya vemos que ninguno de los números sean iguales
	#Y validamos que el el primer número sea el mayor de los tres 
    print(f"{iNumero1} es mayor que {iNumero2} y {iNumero3}")
elif iNumero2 > iNumero1 and iNumero2 > iNumero3:
    #Aquí validamos que el segundo numero sea el mayor de los tres
    print(f"{iNumero2} es mayor que {iNumero1} y {iNumero3}")
else:
    #Por descarte, eneste último validamos que el tercer 
	#número sea el mayor de los tres
    print(f"{iNumero3} es mayor que {iNumero1} y {iNumero2}")
#fin del if-else
