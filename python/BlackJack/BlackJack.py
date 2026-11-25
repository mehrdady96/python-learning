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
        value = { 1 : 'A' ,
                2 : 2 , 
                3 : 3 ,
                4 : 4 , 
                5 : 5 ,
                6 : 6 , 
                7 : 7 ,
                8 : 8 ,
                9 : 9 ,
                10 : 'K' ,
                11 : "Q" , 
                12 : 'J' ,
                }
        return value[card]


    def check_value(self,deck):
        replacement = {
             "A" : 1 ,
             "K" : 10,
             "Q" : 10,
             "J" : 10
        }
        
        aces = 0
        total = 0
        for card in deck:
             if card in replacement :
                  total += replacement[card]
             else:
              total += card
        aces = deck.count("A")
        if aces == 1 and total + 10 <= 21:
            total += 10
        return total


    def check_status(self, player_cards , house_cards) :
        player = self.check_value(player_cards)
        house = self.check_value(house_cards)
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
            elif player == 21 :
                    status = "Player"
            else :
                    status = "seventeen"

        return status





def run():
    blackjack = Blackjack()
    playing = True
    print(" Welcome to MADMAN Casino")
    while playing:

        player_cards = [blackjack.draw_card(randint(1,12)) , blackjack.draw_card(randint(1,12))]
        house_cards = [blackjack.draw_card(randint(1,12)) , blackjack.draw_card(randint(1,12))]
        the_status = blackjack.check_status(player_cards , house_cards)
        print("==========================")
        print(f"Yara has drawn card")
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
                                print(f" { (player_cards) = } , {(house_cards) = }")
                                break
                            if the_status == "House" :
                                print("==========================")
                                print(f" House won")
                                print(f" { (player_cards) = } , {(house_cards) = }")
                                break
                if the_status == "Player":
                    print("==========================")
                    print(f" Player won")
                    print(f" { (player_cards) = } , {(house_cards) = }") 
                    break
                if the_status == "Busted":
                    house_cards.pop()
                    print("==========================")
                    print(f" House won")
                    print(f" { (player_cards) = } , {(house_cards) = }") 
                    break
                if the_status == "Pushed":
                    print("==========================")
                    print(f" PUSHED")
                    print(f" { (player_cards) = } , {(house_cards) = }")
                    break
                if the_status == "House":
                    print("==========================")
                    print(f" House won")
                    print(f" { (player_cards) = } , {(house_cards) = }")
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
                            print(f" { (player_cards) = } , {(house_cards) = }")
                            break
                        if the_status == "House" :
                            print("==========================")
                            print(f" House won")
                            print(f" { (player_cards) = } , {(house_cards) = }")
                            break
                if the_status == "Player":
                    print("==========================")
                    print(f" Player won")
                    print(f" { (player_cards) = } , {(house_cards) = }") 
                    break
                if the_status == "Busted":
                    house_cards.pop()
                    print("==========================")
                    print(f" House won")
                    print(f" { (player_cards) = } , {(house_cards) = }") 
                    break
                if the_status == "Pushed":
                    print("==========================")
                    print(f" PUSHED")
                    print(f" { (player_cards) = } , {(house_cards) = }")
                    break
                if the_status == "House":
                    print("==========================")
                    print(f" House won")
                    print(f" {(player_cards) = } , {(house_cards) = }")
                    break
                house_cards.append(blackjack.draw_card(randint(1,12)))
                the_status = blackjack.check_status(player_cards , house_cards)
        choice = input(" Press Enter to play , (no for exit)")
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


if __name__  == "__main__":
     run()
