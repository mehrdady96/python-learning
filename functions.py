# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:21:15 2026

@author: mad man
"""


def is_even(n):
 
    return n % 2 == 0


def get_odds(nums):
    odds = []
    count = 0
    
    for num in nums:
        if not is_even(num):
            odds.append(num)
            count += 1
            
    return  count, odds



numbers = list(range(10))
count , odds = get_odds(numbers)
print (count,odds , sep = ' , ')

