# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#def FunctionName(Input):
#    Action
#    return Output


def addOne (Number):
    Output = Number + 1 
    return Output 

Var = 0 
print(Var) #0
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(Var3)
Var5 = addOne(2)
Var6 = addOne(2.1)
Var7 = addOne(2.1+3.4)
print(Var2)#1
print(Var3)#2
print(Var4)#3
print(Var5)#3
print(Var6)#3.1
print(Var7)#6.5


def addOneAddTwo (NumberOne, NumberTwo):
    Output = NumberOne + 1
    #Output = Output + NumberTwo +2 
    Output += NumberTwo + 2
    return Output

Sum = addOneAddTwo(1,2)
#return 6 because fisrt output = 1 + 1 =2
#the second output = 2 + 2 = 4 
# then 2 + 4 = 6 

print(Sum)

Sum = addOneAddTwo(Var,Var2)
#Var = 0 then output = (Var = 0) + 1 = 1
#Var2 = addOne(Var)
#Var2 = addOne(0)
#Var2 = 0 + 1 = 1 
#Second output = (Var2 = 1) + 2 = 3 
#then 1 + 3 = 4
print(Sum)

Sum = addOneAddTwo(Var2,Var3)
#Var2 = addOne(Var)
#Var2 = addOne(0)
#Var2 = 0 + 1 = 1 
#Var3 = addOne(Var2)
#Var3 = 1 + 1 = 2
#Then first output = (Var2 = 1)  + 1
#first output = 1 + 1 = 2 
#second output = (Var3 = 2 ) + 2 
#second output = 2 + 2 
#then 2 + 4 = 6
print(Sum)