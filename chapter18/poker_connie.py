from card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute rank.
        """
        self.rank = {}
        for card in self.cards:
            self.rank[card.rank] = self.rank.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self):
        self.rank_hist()
        for val in self.rank.values():
            if val >= 2:
                return True
        return False

    # def has_twopair(self):
    #     self.rank_hist()
    #     l = sorted(self.rank.values(), reverse=True)
    #     if l[0] >= 2:
    #         if l[1] >= 2:
    #             return True
    #         return False
    #     return False

    def has_twopair(self):
        self.rank_hist()
        l = sorted(self.rank.values(), reverse=True)
        return l[0] >= 2 and l[1] >= 2

    def has_three(self):
        self.rank_hist()
        for val in self.rank.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        self.rank_hist()
        sorted(self.rank)
        if check_consecutive(sorted(self.rank, reverse=True)[:5]):
            return True
        return False

    def has_fullhouse(self):
        self.rank_hist()
        l = sorted(self.rank.values(), reverse=True)
        if l[0] >= 3:
            if l[1] >= 2:
                return True
            return False
        return False

    def has_four(self):
        self.rank_hist()
        for val in self.rank.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self):
        self.suit_hist()
        self.rank_hist()
        for val in self.suits.values():
            if val >= 5:
                if check_consecutive(sorted(self.rank, reverse=True)[:5]):
                    return True
                return False
        return False


def check_consecutive(l):
    return sorted(l) == list(range(min(l), max(l) + 1))


def classify(self):
    self.label = None
    if self.has_pair():
        self.label = "pair"
    if self.has_twopair():
        self.label = "two pair"
    if self.has_three():
        self.label = "three"
    if self.has_straight():
        self.label = "straight"
    if self.has_flush():
        self.label = "flush"
    if self.has_fullhouse():
        self.label = "fullhouse"
    if self.has_four():
        self.label = "four"
    if self.has_straight_flush():
        self.label = "straight flush"


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    return d


def class_hist(num_hands, num_cards, num_sim):
    l = []
    for _ in range(num_sim):
        deck = Deck()
        deck.shuffle()
        for _ in range(num_hands):
            hand = PokerHand()
            deck.move_cards(hand, num_cards)
            hand.sort()
            classify(hand)
            l.append(hand.label)

    hist = {
        "pair": 0,
        "two pair": 0,
        "three": 0,
        "straight": 0,
        "flush": 0,
        "fullhouse": 0,
        "four": 0,
        "straight flush": 0,
        **histogram(l),
    }

    return hist


if __name__ == "__main__":
    hands = 7
    cards = 7
    decks = 1000000
    simulations = decks * hands
    hist = class_hist(hands, cards, decks)

    print(f"{simulations} Simulations")
    for key, value in hist.items():
        print(f"{(value / simulations) * 100:10.3f}\t{key}")
