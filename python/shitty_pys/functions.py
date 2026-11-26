# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:18:14 2026

@author: mad man
"""
def largest ():
    largest_number = numbers[0]
    for n in numbers:
        if largest_number < n:
            largest_number = n
    return largest_number

numbers = [1,2,4,7,8,5]
print(largest())



