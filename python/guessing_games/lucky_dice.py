# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:28:51 2026

@author: mad man

user guesses a random number
"""

from random import randint         
user = int(input("Enter your guess between 1 to 6: "))
Human = 0
Machine = 0 
while True:
    luck_numb = randint(1,6)
    if user == luck_numb or user == luck_numb :
        Human += 1
        print(f"YOU WON!!! It was {a}\nHuman:{Human} ,Machine:{Machine}\nKeep Going!!!")
        choice = (input("Try again or enter to exit: "))
        if choice == '' :
            break                   
    else:  
        Machine += 1
        print(f"YOU LOST!!! It was {a}\nHuman:{Human} ,Machine:{Machine}")
        choice = (input("Try again or enter to exit: "))
        if choice == '' :
            break
    
