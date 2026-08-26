# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:01:56 2026

@author: mad man

checks the given name to the data base
"""
people = {
'Mehrdad'   :   {'age' : 24, 'height' : 180}, 
'Kimia'     :   {'age':18, 'height': 160},
'Ali'       :   {'age':36, 'height': 170}
      }
names =[]
while True:
    name = input('Enter the name: ')
    if name == '' :
        break
    names.append(name)
for name in names:
        if name in people:
            print(f"{name} is registerd and the age is {people[name]['sen']} and {people[name]['age']} height")
        else:
            print(f'{name} is not registered and Unknown')
