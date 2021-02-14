n = int("10")

print(n)

n = float("10.8")

print(n)

n = str(10)

print(n)

n = str(10.58)

print(n)

n = bin(10)

#bin devuleve el valor que esta dentro del parentesis pero en formato binario

print(n)

n = hex(10)

#hex deuvlve el valor que esta dentro del parentesis pero en formato hexadecimal

print(n)

n = int("0b1010",2)

#En este caso el valor que esta en binario lo devuelve como un entero 
#La como y el numero indica en que base esta.
#En este caso esta en base 2 

print(n)

n = int("0xa",16)

print(n)

n = abs(-8)

#abs devuelve el valor absoluto de un número

print(n)

n = round(5.6)

#round redondea el valor de un número 

print(n)

n = round(5.4)

#round redondea el valor de un número 

print(n)

n = len("Freddy")

#len devuelve cuantos caracteres tiene una cadena 

print(n)

#Valor absoluto de un número

numero = int(input("Ingresa un numero (entero): "))

print(f"El valor absoluto de {numero} es: ", abs(numero))

#Redondear un número

numero = float(input("Ingresa otro numero (flotante) :"))

print(f"Al redondear tu numero {numero} es: ",round(numero))
    
nombre = input("Ingresa un nombre: ")

print(f"El nombre {nombre} contiene ",len(nombre)," caracteres")

