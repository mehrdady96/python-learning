# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:01:56 2026

@author: mad man
"""
people = {
'Mehrdad'   :   {'sen' : 24, 'ghad' : 180}, 
'Kimia'     :   {'sen':18, 'ghad': 160},
'Ali'       :   {'sen':36, 'ghad': 170}
      }
names =[]
while True:
    name = input('Enter the name: ')
    if name == '' :
        break
    names.append(name)
for esm in names:
        if esm in people:
            print(f"{esm} is registerd and the age is {people[esm]['sen']} and {people[esm]['ghad']} height")
        else:
            print(f'{esm} is not registered and Unknown')