'''
OperadoresRelacionales
+Se utiliza para establecer una relación entre dos valores
+Compara estos valores entre si y esta comparación 
produce un resultado de verdadero o falso 
+Tiene el mismo nivel de prioridad que una evaluación 
+Los operadores relacionales tiene menor prioridad 
que los aritmeticos 

> Mayor que
< Menor que 
>= Mayor que o igual a 
<= Menor que o igual a
!= Diferente de 
== Igual a
'''

resultado = 10 > 20

print(resultado)
#False

resultado = 10 < 20

print(resultado)
#True

resultado = 10  == 20

print(resultado)
#False

resultado = 10  != 20

print(resultado)
#True

resultado = 10  >= 20

print(resultado)
#False

resultado = 10  <= 20

print(resultado)
#True

resultado = 10  <= 10

print(resultado)
#True

resultado = 10  >= 20

print(resultado)
#False

NumeroA = 10
NumeroB = 20
NumeroC = 30

resultado = (NumeroA + NumeroB) == NumeroC

print("El resultado de suma ",NumeroA," + ",NumeroB," = ",NumeroA+NumeroB,resultado)




