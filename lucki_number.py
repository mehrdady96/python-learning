# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:28:51 2026

@author: mad man
"""
from random import randint         
b = int(input("Enter your guess between 1 to 6: "))
while True:
    a = randint(1,6)
    if b == a : 
        print(f"YOU WON!!! It was {a}\nKeep Going!!!")
        c = input("Press Y to continue or Q to exit: ").strip().lower()
        if c == 'y':
            b = int(input("Enter your guess between 1 to 6: "))
            continue
        if c == 'q':
            break                   
    else:        
        print(f"YOU LOST!!! It was {a}")
        b = int(input("Try again or enter to exit: "))
        if b == '' :
            break
    
