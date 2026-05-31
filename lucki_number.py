# -*- coding: utf-8 -*-
"""
Created on Sun May 31 01:28:51 2026

@author: mad man
"""
from random import randint
b = int(input("Enter your guess between 1 to 6: "))
while True:
    a = randint(1,6)
    if a == b:
        print(f"YOU WON!!! It was {a}\nKeep Going!!!")
        break
    else:
        print(f"YOU LOST!!! It was {a}")
        b = int(input("Try again: "))
    