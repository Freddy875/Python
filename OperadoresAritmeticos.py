#Operaadores Aritmeticos

Resultado1 = 10 + 5 ;

print(Resultado1)

Num1 = 10

Num2 = 3
#Aunque en python no declaramos el tipo de dato Num1 y Num2 son números enteros
Suma = Num1 + Num2
#Suma

print("El resultado de sumar ", Num1," + ", Num2, " = ", Suma)

#Resta

#Sobreescribimos los valores de Num1 y Num2
Num1 = 5

Num2 = 10

Resta = Num1 - Num2

print("El resultado de restar ",Num1," - ",Num2," = ",Resta)
#Como Num1 es mas pequeño que Num2 este da como resultado un número negativo (-5)

#Volvemos a sobreescribir los valores de Num y Num2
#Los regresamos a su valor original 
Num1 = 10

Num2 = 3

Resta = Num2 - Num1

#Restamos para obtener un numero negativo

print("El resultado de restar ",Num2," - ",Num1," = ",Resta)

Resta = Num1 - Num2

#Restamos para obtener un numero positivo

print("El resultado de restar ",Num1," - ",Num2," = ",Resta)

#Multiplicación

Mult = Num1 * Num2

print("El resultado de multiplicar ",Num1, " * ",Num2," = ",Mult)

#División

Div = Num1/Num2

#Como Num1 = 10 no es multiplo de Num2 = 3 este da como resultado un número decial
#Por lo tanto Num1 y Num2 dejan de ser enteros y ahora son flotantes o reales

print("El resultado de dividir ",Num1," / ",Num2," = ",Div)

#Modulos

Mod = Num1%Num2

print("El residuo de dividir ",Num1," / ",Num2," = ",Mod)

#Potencia 
#Sobreescribimos los valores de Num1 y Num2
Num1 = 2
Num2 = 5

Potencia = Num1**Num2

print("El resultado de elevar ",Num1," a la potencia",Num2," es ",Potencia)

'''
Prioridad de los operadores aritmeticos 
1. Parentesis ()
2. Exponenciación **
3. Multiplicación, División y Modulo *,/,%
4. Suma y Resta +,-
'''

'''
Obtener el resultado de 
3 a la tercera potencia 
que multiplica a 
13/5 menos (2x4)
'''

Resultado1 = 3**3 * (13/5 - (2 * 4))

print(Resultado1)

#División excata

Num1 = 2
Num2 = 5


DivisionExacta = Num2//Num1

print("El resultado cerrado de dividir",Num2, " / ", Num1, " = ", DivisionExacta)

mensaje = """Esto es un mensaje 
    con tres saltos
    de linea"""

print(mensaje)


