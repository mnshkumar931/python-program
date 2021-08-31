import random
suits=('hearts','diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14} 
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

# y=Card('heart','two')
# print(y.suit)
# print(y.rank)
# print(y)
# print(values[y.rank])
# z=Card('dimond','king')
# print(z.rank)
# print(values[z.rank])
# print( y.value>z.value)

class Deck:
    def __init__(self):
        self.all_cards=[]
    
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def suffle(self):
        random.shuffle(self.all_cards)
               
# new_deck = Deck()
# bottom_card=new_deck.all_cards[-1]
# print(bottom_card)
# for card_object in new_deck.all_cards:
#     print(card_object)
# new_deck.suffle()
# nbottom_card=new_deck.all_cards[-1]
# print(nbottom_card)
# for card_object in new_deck.all_cards:
#     print(card_object)
    def deal_one(self):

         return self.all_cards.pop()
new_deck=Deck()
new_deck.suffle()
my_card=new_deck.deal_one()
print(my_card)
print(len(new_deck.all_cards))
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        
        if type(new_cards)==type([]):
            #list of multiple card object
            self.all_cards.extend(new_cards)
        else:
            #only has one card object
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards '
new_player=Player('manish')
print(new_player)
new_player.add_cards(my_card)
print(new_player)
print(new_player.all_cards[0])
new_player.add_cards([my_card,my_card,my_card])
print(new_player)
new_player.remove_one()
print(new_player)

#GAME SETUP
player_one=Player('one')
player_two=Player('two')

new_deck=Deck()
new_deck.suffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num=0
while game_on:
    round_num+=1
    print(f'round {round_num}')
    if len(player_one.all_cards) == 0:
        print('player one is out of card!,player two won')
        game_on=False
        break
    if len(player_two.all_cards) == 0:
        print('player two is out of card!,player one won')
        game_on=False
        break

    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war=False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war=False
        else:
            print('WAR!')
            if len(player_one.all_cards)<5:
                print('player one unable to declare war')
                print("player two won")
                game_on=False
                break
            elif len(player_two.all_cards)<5:
                print('player two unable to declare war')
                print("player one won")
                game_on=False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

