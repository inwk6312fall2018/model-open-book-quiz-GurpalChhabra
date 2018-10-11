class Cards(object):
    suits=('club','diamond','heart','spade')
    cardsnum=('A','2','3','4','5','6','7','8','9','10','j','q','k',)

    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit

class Deck(object):
    def __init(self,deck):
        self.deck=[]
        for suit in Cards.suits:
            for cards in Cards.cardsnum:
                card = Cards(rank, suit)
                self.deck.append(card)
    def shuffle (self):
        random.shuffle(self.deck)

class Poker():
    def __init__ (self, numHands):
      self.deck = Deck()
      self.deck.shuffle ()
      self.hands = []
      playcards_in_Hand = 5
  
      for i in range (numHands):
          hand = []
          for j in range (numCards_in_Hand):
              hand.append (self.deck.deal())
              self.hands.append (hand)



