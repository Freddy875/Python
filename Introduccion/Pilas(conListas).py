#Pilas

#Las pilas pueden emularse con Listas
#Las pilas son una estructura de datos 
#de tipo LIFO (Last In-First Out)

pila = [1,2,3]

print(f"La pila inicila {pila}")

#Agregar elementos por el final de la pila 

pila.append(4)
pila.append(5)

print(f"La pila despues de agregar dos valores {pila}")

#Sacar elementos de la pila por el final 

variableN = pila.pop()

print(f"Sacando el ultimo elemento {variableN} de la pila {pila}")

#El metodo pop ademas de sacar el ultimo elemento tambien lo retorna 
