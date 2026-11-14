"""
A model to play black jack 
Joker card is discard
"""
from random import randint


class Blackjack():
    def draw_card(self, card):
        """
        checks the value of each card
        """
        if card == 1:
            card = 'A'
        if card == 10 :
            card = 'K'
        if card == 11:
            card = 'Q'
        if card == 12:
            card = 'J'
        value = {'A' : 1 ,
                2 : 2 , 
                3 : 3 ,
                4 : 4 , 
                5 : 5 ,
                6 : 6 , 
                7 : 7 ,
                8 : 8 ,
                9 : 9 ,
                'K' : 10 ,
                'Q' : 10 , 
                'J' : 10 ,
                }
        return value[card]


    def value_of_ace(self, card_one , card_two):
        """
        checks value of ace
        """
        if Blackjack.draw_card(card_one) + Blackjack.draw_card(card_two) <= 10 and not(card_one == 1 or card_two == 1 ) :
            ace = 11
        elif  Blackjack.draw_card(card_one) + Blackjack.draw_card(card_two) > 10 or (card_one == 1 or card_two == 1 ):
            ace = 1
        return ace


    def check_value(self,deck):
        aces = 0
        total = sum(deck)
        aces = deck.count(1)
        if aces == 1 and total + 10 <= 21:
            total += 10
        return total


    def check_status(slef, player_cards , house_cards) :
        player = sum(player_cards)
        house = sum(house_cards)
        status = ''
        if house > 21 :
            if player <= 21 :
                    status = "Player"
            if player > 21 :
                    status = "Busted"
        if house == 21 :
                if player == 21 :
                    status = "Pushed"
                else :
                    status = "House"
        if house < 21 and house != 17 :
            if player == 21 :
                    status = "Player"
            if player > 21 :
                    status = "House"
        if house == 17 :
            if player > 21 :
                    status = "House"
            if player == 21 :
                    status = "Player"
            else :
                    status = "seventeen"

        return status




blackjack = Blackjack()
playing = True
print(" Welcome to MADMAN Casino")
while playing:
    player_cards = [blackjack.draw_card(randint(1,12)) , blackjack.draw_card(randint(1,12))]
    house_cards = [blackjack.draw_card(randint(1,12)) , blackjack.draw_card(randint(1,12))]
    the_status = blackjack.check_status(player_cards , house_cards)
    print("==========================")
    print(f"Yare has drawn card")
    print(f" {player_cards = } , {house_cards = }")
    choice = ""
    while choice not in ("H", "S"):
        choice = input(" Hit or Stand ?:(H/S) ").upper()


    while True :
        if choice == "H" :
            if the_status == "seventeen" :
                while True :
                        player_cards.append(blackjack.draw_card(randint(1,12)))
                        the_status = blackjack.check_status(player_cards , house_cards)
                        if the_status == "Player" :
                            print("==========================")
                            print(f" Player won")
                            print(f" {player_cards = } , {house_cards = }")
                            break
                        if the_status == "House" :
                            print("==========================")
                            print(f" House won")
                            print(f" {player_cards = } , {house_cards = }")
                            break
            if the_status == "Player":
                print("==========================")
                print(f" Player won")
                print(f" {player_cards = } , {house_cards = }") 
                break
            if the_status == "Busted":
                house_cards.pop()
                print("==========================")
                print(f" House won")
                print(f" {player_cards = } , {house_cards = }") 
                break
            if the_status == "Pushed":
                print("==========================")
                print(f" PUSHED")
                print(f" {player_cards = } , {house_cards = }")
                break
            if the_status == "House":
                print("==========================")
                print(f" House won")
                print(f" {player_cards = } , {house_cards = }")
                break

            player_cards.append(blackjack.draw_card(randint(1,12)))
            house_cards.append(blackjack.draw_card(randint(1,12)))
            the_status = blackjack.check_status(player_cards , house_cards)


        if choice == "S" :
            if the_status == "seventeen" :
                while True :
                    player_cards.append(blackjack.draw_card(randint(1,12)))
                    the_status = blackjack.check_status(player_cards , house_cards)
                    if the_status == "Player" :
                        print("==========================")
                        print(f" Player won")
                        print(f" {player_cards = } , {house_cards = }")
                        break
                    if the_status == "House" :
                        print("==========================")
                        print(f" House won")
                        print(f" {player_cards = } , {house_cards = }")
                        break
            if the_status == "Player":
                print("==========================")
                print(f" Player won")
                print(f" {player_cards = } , {house_cards = }") 
                break
            if the_status == "Busted":
                house_cards.pop()
                print("==========================")
                print(f" House won")
                print(f" {player_cards = } , {house_cards = }") 
                break
            if the_status == "Pushed":
                print("==========================")
                print(f" PUSHED")
                print(f" {player_cards = } , {house_cards = }")
                break
            if the_status == "House":
                print("==========================")
                print(f" House won")
                print(f" {player_cards = } , {house_cards = }")
                break
            house_cards.append(blackjack.draw_card(randint(1,12)))
            the_status = blackjack.check_status(player_cards , house_cards)
    choice = input(" Press Enter to play")
    if choice == '':
         pass
    else :
         tip = False
         mind = input(" Did you tipped Yara ? >:( ")
         while not tip :
                if mind == "yes":
                    print(" Thank you")
                    input(" Goodbye :)")
                    playing = False
                    break
                else :
                     mind = input(" Did you tipped Yara ? >:( ")
