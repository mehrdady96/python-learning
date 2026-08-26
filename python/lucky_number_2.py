"""
created on Friday june 3:18 19/06/2026
@athur : MadMAn

user guesses a random number
"""
def welcome():
    '''
    showing welcome messages for the firts time
    '''
    print("Welcome to this funny game!!!")
    print("Machine picks a number between 1 to 9 and you have to guest it!!!")

def finish():
    '''
   asking user for finish or new game
   '''
    print("Good game!!!")
    answer = input("Do you want to try again?(Y/N)??? ")
    return answer.upper() == "Y"



def win (guess,secret_number):
    '''
    checks if user has won
    '''
    return guess == secret_number


def check(guess, computer):
    '''
    checks user number with random number
    '''
    if guess == computer:
        return 'THATS RIIIIIGHT!!!'
    if guess > computer:
        return 'pick lower!!!!'
    if guess < computer:
        return 'PICK HIGHER!!!'
    return None

def get():
    '''
    gets user number
    '''
    return int(input("Enter youre guess here: "))


def records(count, the_best):
    '''
    registers user recods
    '''
    if count == 0 and the_best is None:
        return "UNBEATBLE!!!" , the_best
    if the_best is None:
        the_best = count
        if count == 1:
            message = "The very first record. It took you 1 time "
            return message, the_best
        if count > 1:
            message = f"The very first record. It took you {count} times "
            return message, the_best

    if count < the_best:
        message = f"The last record was {the_best}, Now is {count}"
        the_best = count
        return message , the_best
    if count == 0 and the_best > 0:
        message = f"The last record was {the_best}, and you guested with zero efforts!!!"
        return message , the_best
    else:  
      message = f"It took you {count} times. The record is {the_best}"
      return message , the_best


welcome()
the_best = None
continue_playing = True
while continue_playing:
    user = 0
    count = 0
    import random
    computer_number = random.randint(1,9)
    while not win(user,computer_number):
        user = get()
        print(check(user,computer_number))
        if user != computer_number:
            count += 1
        if user == computer_number:
            message , the_best = records(count, the_best)
            print(message)
            continue_playing = finish()
