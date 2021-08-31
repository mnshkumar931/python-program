import random
suits=('heart','diamond','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank  + " of " + self.suit
b=Card('heart','two')
print(b)
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
           for rank in ranks:
               created_card=Card(suit,rank)
               self.all_cards.append(created_card)
    def shuffle(self):
        return random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop(51)
a=Deck()
print(a)
for card_object in a.all_cards:
    print(card_object)        
# a.shuffle()
# for card_object in a.all_cards:
#     print(card_object)     
m=a.deal_one()
print(m)
print(len(a.all_cards))
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
       

    