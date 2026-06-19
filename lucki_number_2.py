"""
created on Friday june 3:18 19/06/2026
@athur : MadMAn
"""
def welcome():
    print("Welcome to this funny game!!!")
    print("Machine picks a number between 1 to 9 and you have to guest it!!!")

def finish():
    print("Good game!!!")
    print(f"You founded the mahcine number and it was {computer_number} !!!")


def check(adam, computer):
    
    if adam == computer:
        return 'Dorost Gofti!!!'
    
    if adam > computer:
        return 'Payin Taaaar!!!!'
    
    if adam < computer:
        return 'Balataaaaaar!!!'

def get():
    return int(input("Enter youre number here: "))
    

def win (human, computer_number):
    return human == computer_number

import random 
computer_number = random.randint(1,9)


while True:
    user = get()
    print(check(user,computer_number))
    if user == computer_number:
        finish()
        break