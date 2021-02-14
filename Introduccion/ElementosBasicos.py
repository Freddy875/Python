#Determinar la solucion basica de 
#(3+5*8)<3 and (((-6/3) * 4)+2<2) or (a>b)

iResultado1 = (3+5*8)

print(iResultado1)

iResultado1 = (3+5*8)<3

print(iResultado1)

iResultado2 = (((-6/3)*4)+2)

print(iResultado2)

iResultado2 = (((-6/3)*4)+2)<2

print(iResultado2)

iResultado3 = (3+5*8)<3 and (((-6/3)*4)+2)<2

print(iResultado3)

iNumeroA = int(input("Ingresa el valor de A (entero) :"))

iNumeroB = int(input("Ingresa el valor de B (entero) :"))

iResultado4 = (3+5*8)<3 and (((-6/3)*4)+2)<2 or (iNumeroA > iNumeroB)

print(iResultado4)

