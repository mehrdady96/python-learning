# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:28:51 2026

@author: mad man
"""

from random import randint         
b = int(input("Enter your guess between 1 to 6: "))
Human = 0
Machine = 0 
while True:
    a = randint(1,6)
    if b == a or b == 7:
        Human += 1
        print(f"YOU WON!!! It was {a}\nHuman:{Human} ,Machine:{Machine}\nKeep Going!!!")
        b = (input("Try again or enter to exit: "))
        if b == '' :
            break                   
    else:  
        Machine += 1
        print(f"YOU LOST!!! It was {a}\nHuman:{Human} ,Machine:{Machine}")
        b = (input("Try again or enter to exit: "))
        if b == '' :
            break
    
