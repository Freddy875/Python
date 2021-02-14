#Colas

from collections import deque 
#Importando el modulo coleccion 
#e importando el modulo deque 

#Estructuras de datos de tipo FIFO
#(Fisrt In-First Out)
#Cola de personas del banco

cola = ["Maria","Alejandro","Jose","Mario"]

print(cola)

#Agregar mas elementos al final d euna lista

cola.append("Karla")
cola.append("Flor")

print(cola)

#Sacando elementos por el principio de la cola 

#Usar directamente el metodo pop hara que salga el ultimo elemento
#Pero como queremos que salga el primero le indicamos con el indice 

VariableN = cola.pop(0) 

print(f"Ahora estan atendiendo en el banco a {VariableN}")

print(f"En la cola del banco ahora quedan {cola}")

VariableN = cola.pop(0) 

print(f"Ahora estan atendiendo en el banco a {VariableN}")

print(f"En la cola del banco ahora quedan {cola}")
