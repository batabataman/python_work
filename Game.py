from Deck import Deck
from Player import Player
from Card import Card
class Game:
    game_cards =[]
    def __init__(self):
        name1 = input("player name:")
        name2 = input("player name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.card = Card(10, 2)
        self.game_cards.append(Card(11,3))

    def wins(self, winner):
        w = "this game winner is {}"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、{}は{}を引きました"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争をはじめます")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            print(type(p1c))
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p1c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("ゲーム終了です。{}の勝利です。".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()
