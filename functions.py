# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:18:14 2026

@author: mad man
"""
def is_even(n):
    return (n % 2 == 0)

def even(nums):
    for n in nums :
        if is_even(n):
            return True
    return False



my_numbers =  [1,2,3,4,5,6,7,8,9]

print(even(my_numbers))




