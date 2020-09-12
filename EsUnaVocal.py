#Pedir un caracter e indicar si es una vocal o no 

cLetra = input("Ingresa una letra: ")

#cLetra = cLetra.lower()
#esta es otra forma de hacerlo

#La operacion contraria a lower es upper

#cLetra = input("Ingresa una letra: ").upper()


if cLetra == 'a'or cLetra == 'e' or cLetra == 'i' or cLetra == 'o' or cLetra == 'u':
    print(f"Tu letra {cLetra} es una vocal y es minuscula")
elif cLetra == 'A' or cLetra == 'E' or cLetra == 'I' or cLetra == 'O' or cLetra == 'U':
    print(f"Tu letra {cLetra} es una vocal y es Mayuscula")
else:
     print(f"Tu letra {cLetra} NO es una vocal")