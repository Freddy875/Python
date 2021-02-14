#Condicionales

iNumero = int(input("Ingresa un numero (entero): "))

if iNumero>0:
    print(f"Tu numero {iNumero} es positivo")
elif iNumero == 0:
#elif es el equivalente en python a if-else
    print(f"Tu numero {iNumero} es cero")
else:
    print(f"Tu numero {iNumero} es negativo")
#fin if-else

print("Fin del programa ")