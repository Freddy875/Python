# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:55:57 2021

@author: fer87
"""

BlackShoes = {42:2,41:3,40:4,39:1,38:0}
print(BlackShoes)
while(True):
        purchaseSize = int(input("Which shoes size would you like to buy?\n"))
        if purchaseSize < 0:
            break
        if BlackShoes[purchaseSize] > 0:
            BlackShoes[purchaseSize] -= 1
        else:
            print("Shoes are no longer in stcok")
        print(BlackShoes)
        
        
        
        