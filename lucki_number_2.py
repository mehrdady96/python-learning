"""
created on Friday june 3:18 19/06/2026
@athur : MadMAn
"""
def welcome():
    print("Welcome to this funny game!!!")
    print("Machine picks a number between 1 to 9 and you have to guest it!!!")

def finish():
    print("Good game!!!")
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

def records():
    global the_best
    if the_best == count and count== 0:
        return "UNBEATBLE!!!"
    if the_best == 0 :  
        the_best = count
        if count == 1:
            return(f"The very first record. It took you 1 time ")    
        if count > 1:
            return(f"The very first record. It took you {count} times ")  
    if count < the_best: 
        the_old_record = the_best
        the_best = count
        return(f"The last record was {the_old_record}, Now is {count}")
    if count == 0 and the_best > 0:
        return(f"The last record was {the_old_record}, and you guested with zero effort!!!")
    else:
        return(f"It took you {count} times. The record is {the_best}")
welcome()
continue_playing = True


the_best = 0
while (continue_playing):
        user = 0
        count = 0
        import random 
        computer_number = random.randint(1,9)
        while (not win(user,computer_number)):
            user = get()
            print(check(user,computer_number))
            if user != computer_number:
                count += 1
            if user == computer_number:
                print(records())
                continue_playing = finish()
