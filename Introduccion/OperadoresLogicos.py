#Operadores Lógicos 
#Permite construir expresiones lógica 
#Se obtiene como resultado booleanos 
#Prioridad de los operadores lógicos
# 1. NOT
# 2. AND
# 3. OR
# Prioridad de los operadores en general
# 1. ()
# 2. **
# 3. *,/,mod,not 
# 4. +,-, and 
# 5. >,<,==,>=,<=,!=,or
# 
NumeroA = 10
NumeroB = 15
NumeroC = 20

resultado = ((NumeroA<NumeroB) and (NumeroB<NumeroC))

print(resultado)

resultado = ((NumeroA>NumeroB) or (NumeroB<NumeroC))

print(resultado)

resultado = not((NumeroA>NumeroB) or (NumeroB<NumeroC))

print(resultado)



