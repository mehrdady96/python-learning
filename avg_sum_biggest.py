# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:54:50 2026

@author: mad man

sorts the data of donations
"""


donation = {
    'jadi': 20,
    'mehrdad': 30,
    'kimia': 45,
    'gholi': 60,
    'ali': 15,
    }



def sum_donat(sume):
    return sum(donation.values())


def average(donat):
    return sum(donation.values()) // len(donation)


def largest(num):
    person = ''
    largest_number = list(donation.values())[0]
    for name, num in donation.items():
        if largest_number < num :
            largest_number = num
            person = name
    return person, largest_number
 
person , num = largest(donation)
print(f"the sum of donations is {sum_donat(donation)}")
print(f"the average donation is {average(donation)}")
print(f"{person} donated the most with {num}")
        

