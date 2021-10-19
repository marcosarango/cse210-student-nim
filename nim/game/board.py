import random

# TODO: Define the Board class here
class Board:
    """the resposability is to keep track of the piaces in play"""
    def __init__(self):
        """the class instructor"""
        self._piles = []
        self._prepare()
        
    def apply(self, move):
        pile = move.get_pile()
        stones = move.get_stones()
        self._piles[pile] = max(0, self._piles[pile] - stones)
    def is_empty(self):
        """if all the stones have been removed from the board. It returns True if the board has no stones on it;
        false if otherwise. """
        empty = [0] * len(self._piles)
        return self._piles == empty
    def to_string(self):
        """The to_string method converts the board data to its string representation and returns it to the caller. """
        text =  "\n--------------------"
        for pile, stones in enumerate(self._piles):
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        return text
    def _prepare(self):
        """The _prepare method sets up the board with a random number of piles (2 - 5) containing a random number of stones (1 - 9). """
        piles = random.randint(2, 5) 
        for n in range(piles):
            stones = random.randint(1, 9)
            self._piles.append(stones)
        