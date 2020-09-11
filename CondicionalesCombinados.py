#Condicionales combinados 

iEdad = int(input("Ingresa tu edad: "))

#if iEdad>0 and iEdad<100:
#    print("Edad Correcta ")
#    if iEdad>=18:
#        print(f"Tienes {iEdad} y eres mayor de edad")
#    else:
#        print(f"Tienes {iEdad} y eres menor de edad")
#else:
#    print("Edad incorrecta ")

#Otra forma de hacerlo es

#if not (iEdad>0 and iEdad<100):
#    print("Edad incorrecta ")
#else:
#    print("Edad Correcta ")
#    if iEdad>=18:
#        print(f"Tienes {iEdad} y eres mayor de edad")
#    else:
#        print(f"Tienes {iEdad} y eres menor de edad")

#Y otra forma de hacerlo es con un rango 

if 0<iEdad<100:
    print("Edad Correcta ")
    if iEdad>=18:
        print(f"Tienes {iEdad} y eres mayor de edad")
    else:
        print(f"Tienes {iEdad} y eres menor de edad")
else:
    print("Edad incorrecta ")
