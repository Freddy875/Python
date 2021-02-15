'''
Cadenas puede estar rodeados por 
comillas simples o comillas dobles
'''

print("Hello")
print('Hello')

'''
Asignar una cadena a una varible
'''

a = "Can you hear me?"
print(a)

'''
Cadenas en multiples lineas
'''

a = """
Hace mucho tiempo
en una galaxia muy muy lejana
Star Wars: Una nueva esperanza
Son tiempos de guerra civil.
Naves rebeldes han atacado 
desde una base secreta y 
han obtenido su primera
victoria contra el malvado
Imperio Galactico.

Durante la batalla, espias
rebeldes lograron robar los
planos secretos del arma 
mas extrema del Imperio,
la ESTRELLA DE LA 
MUERTE, una estacion
espacial blindada con
suficiente potencia para
destruir un planeta entero.

Perseguida por los
siniestros agentes del
Imperio, la Princesa Leia
se dirige velozmente a casa
en su nave espacial,
mientras resguarda los
planos que pueden salvar
a su pueblo y restaurar la
libertad en la galaxia
"""
print(a)

#Cadenas y arreglos

'''
Una cadena entre corchetes accede a un solo
caracter de la cadena
'''

a = "Star Wars "

print(a[1])

#Bulce a traves de una cadena 

print("\n Bulce a traves de una cadena \n")

for x in "banansas":
    print(x)

#Longitud de una cadena
'''
Para obtener la longitud de una cadena 
usa la funcion len()
'''

print("Longitud de una cadena")

a = "Star Wars"

print(len(a))

#Revisar una cadena
'''
Revisar si cierta frase o carcater esta presente 
en una cadena, podemos usar la palabra clave
in
'''

print("Revisar una cadena")

txt = "Star Wars: Una nueva esperanza"
print("esperanza" in txt)

#Con un if

txt = "Star Wars: Una nueva esperanza"
if "esperanza" in txt:
    print("Si, 'esperanza' esta presente")

#Revisar Si NO esta presente

txt = "Star Wars: Una nueva esperanza"
print("Despertar" not in txt)

#Con un if
txt = "Star Wars: Una nueva esperanza"
if "Despertar" not in txt:
    print("Si, Despertar NO esta presente")
