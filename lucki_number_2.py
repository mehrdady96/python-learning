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
    print()
    answer = input("Do you want to try again?(Y/N)??? ")
    if answer.upper() == "Y":
        return True
    else:
        return False


def win (guess,computer_number):
    return guess == computer_number


def check(adam, computer):
    
    if adam == computer:
        return 'Dorost Gofti!!!'
    
    if adam > computer:
        return 'Payin Taaaar!!!!'
    
    if adam < computer:
        return 'Balataaaaaar!!!'

def get():
    return int(input("Enter youre guess here: "))
   

def win (human, computer_number):
    return human == computer_number



welcome()
continue_playing = True

while (continue_playing):
        user = 0
        import random 
        computer_number = random.randint(1,9)
        while (not win(user,computer_number)):
            user = get()
            print(check(user,computer_number))
            if user == computer_number:
               continue_playing = finish()
