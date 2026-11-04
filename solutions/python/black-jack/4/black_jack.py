"""
A model to play black jack 
Joker card is discard
"""
def value_of_card(card):
    """
    checks the value of each card
    """
    value = {'A' : 1 ,
            '2' : 2 , 
            '3' : 3 ,
            '4' : 4 , 
            '5' : 5 ,
            '6' : 6 , 
            '7' : 7 ,
            '8' : 8 ,
            '9' : 9 ,
            '10' : 10 ,
            'K' : 10 ,
            'Q' : 10 , 
            'J' : 10 ,
            }
    return value[card]


def higher_card(card_one, card_two) :
    """
    A function checks wich card has higher value
    """
    if value_of_card(card_one) < value_of_card(card_two) :
        return card_two
    if value_of_card(card_one) > value_of_card(card_two) :
        return card_one

    return card_one, card_two


def value_of_ace(card_one , card_two):
    """
    checks value of ace
    """
    ace = False
    if value_of_card(card_one) + value_of_card(card_two) <= 10 and not(card_one == 'A' or card_two == 'A' ) :
        ace = 11
    elif  value_of_card(card_one) + value_of_card(card_two) > 10 or (card_one == 'A' or card_two == 'A' ):
        ace = 1
    return ace


def is_blackjack(card_one, card_two):
    """
    checks for black jack
    """
    if card_one == 'A':
        return 11 + value_of_card(card_two) == 21
    if card_two == 'A':
        return 11 + value_of_card(card_one) == 21
    if card_one != 'A' or card_two != 'A':
        return value_of_card(card_one) + value_of_card(card_two) == 21
    return None


def can_split_pairs(card_one, card_two):
    """
    checks if player can split or not
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """
    Determine if the two-card hand can be "doubled down"
    """
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
