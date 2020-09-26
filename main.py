import random

# ______________________Global Variables________________________________

values = {"Two":  2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8
          , 'Nine': 9, "Ten": 10, 'Jack': 11, "Queen": 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ("Two", 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', "Ten", 'Jack' , "Queen", 'King', 'Ace')


# Card class that obtains rank, suit and value
class Card:
    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# Creates a deck and offers functions to shuffle it and deal one card from the bottom
class Deck:
    def __init__(self):
        self.allcards = []

        for rank in ranks:
            for suit in suits:
                created_card = Card(suit, rank)
                self.allcards.append(created_card)

    def deck_shuffle(self):
        random.shuffle(self.allcards)

    def deal_a_card(self):
        return self.allcards.pop()



# Creates a player that have 26 cards. Functions to draw a card for a game
# and add cards to your deck if match is won
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def deal_a_card(self):
        return self.all_cards.pop(0)


# _________________Game Start____________________

# Creates a deck
new_deck = Deck()

# shuffles it
new_deck.deck_shuffle()

# Creates two players
player_one = Player("John")
player_two = Player("Alex")

#Adds 26 cards from deck to player deck
for x in range(26):
    player_one.add_cards(new_deck.deal_a_card())
    player_two.add_cards(new_deck.deal_a_card())

# Starting game
game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Currently on round {round_num}")

    # Checks if players have valid amount of cards
    if len(player_one.all_cards) < 1:
        print(player_one.name + " ran out of cards!" + player_two.name + " have won")
        game_on = False
        break


    if len(player_two.all_cards) < 1:
        print(player_two.name + " ran out of cards!" + player_one.name + " have won")
        game_on = False
        break

    # Adds one card each from players on the table
    player_one_cards = []
    player_one_cards.append(player_one.deal_a_card())

    player_two_cards = []
    player_two_cards.append(player_two.deal_a_card())

    at_war = True


    # Checks card values and adds all cards to coresponding player deck
    # If values are equal "WAR" is declared
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR!")

            # If Player have less than 5 cards game is over
            if len(player_one.all_cards) < 5:
                print(player_one.name + " unable to declare war!")
                print(player_two.name + " have won!")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print(player_two.name + " unable to declare war!")
                print(player_one.name + " have won!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.deal_a_card())
                    player_two_cards.append(player_two.deal_a_card())











