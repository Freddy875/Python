#Acceso a la listas

estalista =["manzana","bananas","cereza"]
print(estalista[1])

#Indice negativo
print(estalista[-1])

#Rango de index
estalista =["manzana","bananas","cereza","naranja","kiwi","limon","melon","mango"]
print(estalista[2:5])

print(estalista[:4])

#Esto devuelve los valores del indice 0 al indice 4

print(estalista[2:])

#Esto devuelve los valores del indice 2 al final

print(estalista[-4:-1])
#Indice negativo empieza desde el final de la lista

#Revisar si un elementos existe

if "manzana" in estalista:
    print("Si, 'manzana' esta en la lista de frutas")


