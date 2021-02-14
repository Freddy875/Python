'''
Simular el comportamiento de una calculadora qe puede realizar las
4 operaciones aritméticas  básicas (suma, resta, multiplicación
y división)
El usuario debe especificar la operación con el primer caracter 
del nombre de la operación.
S,s - suma
R,r - resta
M,m - multiplicación 
D,d - división 
'''

print("Calculadora basica"
,"\nEste programa realiza las 4 operaciones basicas"
,"\nDe dos numeros"
,"\ns o S para suma"
,"\nr o R para resta"
,"\nm o M para multiplicacion"
,"\nd o D para division")

fNumero1 = float(input("Ingresa el primer valor: "))

fNumero2 = float(input("Ingresa el segundo valor: "))

cOperacion = input("Ingresa el simbolo de la operacion: ")

if cOperacion == 'S' or cOperacion == 's':
    fSuma = fNumero1 + fNumero2
    print("Suma: ",
    f"\nEl resultado de sumar {fNumero1} + {fNumero2} = {fSuma}")
elif cOperacion == 'R' or cOperacion == 'r':
    fResta = fNumero1 - fNumero2
    print("Resta: ",
    f"\nEl resultado de restar {fNumero1} - {fNumero2} = {fResta}")
elif cOperacion == 'M' or cOperacion == 'm':
    fMultiplicacion = fNumero1 * fNumero2
    print("Multiplicacion: ",
    f"\nEl resultado de multiplicar {fNumero1} * {fNumero2} = {fMultiplicacion}")
elif cOperacion == 'D' or cOperacion == 'd':
    
    if fNumero2 == 0:
        print("ERROR la division entre cero no esta definida ")
    else:
        fDivision = fNumero1/fNumero2
        print("Division:",
        f"\nEl resultado de dividir {fNumero1} / {fNumero2} = {fDivision}")
else:
    print("Opcion NO Valida ")

