# Card Class & Other Related Classes

TWO_CARD_RANK   = 2
THREE_CARD_RANK = 3
FOUR_CARD_RANK  = 4
FIVE_CARD_RANK  = 5
SIX_CARD_RANK   = 6
SEVEN_CARD_RANK = 7
EIGHT_CARD_RANK = 8
NINE_CARD_RANK  = 9
TEN_CARD_RANK   = 10
JACK_CARD_RANK  = 11
QUEEN_CARD_RANK = 12
KING_CARD_RANK  = 13
ACE_CARD_RANK   = 14

NO_OWNER = -1

class Card:
    """Card class containing rank, and other metadata
    """

    def __init__(self, rank_ : int, owner_ = NO_OWNER):
        """Constructor

        Args:
            rank_ (int): Rank of the Card
            owner_ (int): Owner of the Card
        """
        self.rank  = rank_
        self.owner = owner_

    def getRank(self) -> int:
        """Return the Class Rank

        Returns:
            int: Rank
        """
        return self.rank


class AceCard(Card):
    """Ace Card
    """

    def __init__(self):
        super().__init__(ACE_CARD_RANK)


class TwoCard(Card):
    """Two Card
    """

    def __init__(self):
        super().__init__(TWO_CARD_RANK)


class ThreeCard(Card):
    """Three Card
    """

    def __init__(self):
        super().__init__(THREE_CARD_RANK)


class FourCard(Card):
    """Four Card
    """

    def __init__(self):
        super().__init__(FOUR_CARD_RANK)


class FiveCard(Card):
    """Five Card
    """

    def __init__(self):
        super().__init__(FIVE_CARD_RANK)


class SixCard(Card):
    """Six Card
    """

    def __init__(self):
        super().__init__(SIX_CARD_RANK)


class SevenCard(Card):
    """Seven Card
    """

    def __init__(self):
        super().__init__(SEVEN_CARD_RANK)


class EightCard(Card):
    """Eight Card
    """

    def __init__(self):
        super().__init__(EIGHT_CARD_RANK)


class NineCard(Card):
    """Nine Card
    """

    def __init__(self):
        super().__init__(EIGHT_CARD_RANK)


class TenCard(Card):
    """Ten Card
    """

    def __init__(self):
        super().__init__(TEN_CARD_RANK)


class JackCard(Card):
    """Jack Card
    """

    def __init__(self):
        super().__init__(JACK_CARD_RANK)


class QueenCard(Card):
    """Queen Card
    """

    def __init__(self):
        super().__init__(QUEEN_CARD_RANK)


class KingCard(Card):
    """King Card
    """

    def __init__(self):
        super().__init__(KING_CARD_RANK)

