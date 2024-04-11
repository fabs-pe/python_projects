import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'


def main():
    print('''Blackjack.
          
    Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 0r 11 points.
          Cards 2 through 10 are worth their face value
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.
          
          ''')
    money = 5000

    if money <= 0:
        print("You're broke!")
        print("Good thing you weren't playing with real money")
        print('Thanks for playing!')
        sys.exit()

    print('Money:' , money)
    bet = getBet(money)

    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # HAndle player actions:
    print('Bet:', bet)
    while True:
        displayHands(playerHand, dealerHand, False)
        print()

        # check if player has bust
        #  cont line 59