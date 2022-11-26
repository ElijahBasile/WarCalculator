# GUI that Calculates the War Result

import PySimpleGUI as sg

from Calculator import Calculator
from Card import *

import random

random.seed(20) # DEBUGGING ONLY

NUM_CARDS_IN_DECK = 52

ACE_CARD_IMAGE   = "cards/ace.png"
TWO_CARD_IMAGE   = "cards/two.png"
THREE_CARD_IMAGE = "cards/three.png"
FOUR_CARD_IMAGE  = "cards/four.png"
FIVE_CARD_IMAGE  = "cards/five.png"
SIX_CARD_IMAGE   = "cards/six.png"
SEVEN_CARD_IMAGE = "cards/seven.png"
EIGHT_CARD_IMAGE = "cards/eight.png"
NINE_CARD_IMAGE  = "cards/nine.png"
TEN_CARD_IMAGE   = "cards/ten.png"
JACK_CARD_IMAGE  = "cards/jack.png"
QUEEN_CARD_IMAGE = "cards/queen.png"
KING_CARD_IMAGE  = "cards/king.png"

aceCard   = AceCard()
twoCard   = TwoCard()
threeCard = ThreeCard()
fourCard  = FourCard()
fiveCard  = FiveCard()
sixCard   = SixCard()
sevenCard = SevenCard()
eightCard = EightCard()
nineCard  = NineCard()
tenCard   = TenCard()
jackCard  = JackCard()
queenCard = QueenCard()
kingCard  = KingCard()

eventToCardDict = {
    "ACE":   aceCard,
    "TWO":   twoCard,
    "THREE": threeCard,
    "FOUR":  fourCard,
    "FIVE":  fiveCard,
    "SIX":   sixCard,
    "SEVEN": sevenCard,
    "EIGHT": eightCard,
    "NINE":  nineCard,
    "TEN":   tenCard,
    "JACK":  jackCard,
    "QUEEN": queenCard,
    "KING":  kingCard
}

def isCardEvent(eventString : str):
    """Is this event a card event?

    Args:
        eventString (str): Event String
    """
    return (eventString == "ACE" or
            eventString == "TWO" or
            eventString == "THREE" or
            eventString == "FOUR" or
            eventString == "FIVE" or
            eventString == "SIX" or
            eventString == "SEVEN" or
            eventString == "EIGHT" or
            eventString == "NINE" or
            eventString == "TEN" or
            eventString == "JACK" or
            eventString == "QUEEN" or
            eventString == "KING")


def getCardFromEvent(eventString : str):
    """Given an event, get the card

    Args:
        eventString (str): _description_
    """
    return eventToCardDict[eventString]


def begin(numPlayers : int):
    """This Begins the Calculation of the War Decks

    Args:
        numPlayers (int): Number of Players in Game
    """

    ACE_CARD_BUTTON   = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=ACE_CARD_IMAGE,   image_size=(50, 50), image_subsample=2, border_width=0, key="ACE")
    TWO_CARD_BUTTON   = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=TWO_CARD_IMAGE,   image_size=(50, 50), image_subsample=2, border_width=0, key="TWO")
    THREE_CARD_BUTTON = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=THREE_CARD_IMAGE, image_size=(50, 50), image_subsample=2, border_width=0, key="THREE")
    FOUR_CARD_BUTTON  = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=FOUR_CARD_IMAGE,  image_size=(50, 50), image_subsample=2, border_width=0, key="FOUR")
    FIVE_CARD_BUTTON  = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=FIVE_CARD_IMAGE,  image_size=(50, 50), image_subsample=2, border_width=0, key="FIVE")
    SIX_CARD_BUTTON   = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=SIX_CARD_IMAGE,   image_size=(50, 50), image_subsample=2, border_width=0, key="SIX")
    SEVEN_CARD_BUTTON = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=SEVEN_CARD_IMAGE, image_size=(50, 50), image_subsample=2, border_width=0, key="SEVEN")
    EIGHT_CARD_BUTTON = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=EIGHT_CARD_IMAGE, image_size=(50, 50), image_subsample=2, border_width=0, key="EIGHT")
    NINE_CARD_BUTTON  = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=NINE_CARD_IMAGE,  image_size=(50, 50), image_subsample=2, border_width=0, key="NINE")
    TEN_CARD_BUTTON   = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=TEN_CARD_IMAGE,   image_size=(50, 50), image_subsample=2, border_width=0, key="TEN")
    JACK_CARD_BUTTON  = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=JACK_CARD_IMAGE,  image_size=(50, 50), image_subsample=2, border_width=0, key="JACK")
    QUEEN_CARD_BUTTON = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=QUEEN_CARD_IMAGE, image_size=(50, 50), image_subsample=2, border_width=0, key="QUEEN")
    KING_CARD_BUTTON  = sg.Button(button_color=sg.TRANSPARENT_BUTTON, image_filename=KING_CARD_IMAGE,  image_size=(50, 50), image_subsample=2, border_width=0, key="KING")

    deckSize = int(NUM_CARDS_IN_DECK / numPlayers)

    calculator = Calculator(numPlayers)

    # GUI Layout
    layout = [
        [sg.Text(key="INSTR")],
        [ACE_CARD_BUTTON,  TWO_CARD_BUTTON,   THREE_CARD_BUTTON, FOUR_CARD_BUTTON, FIVE_CARD_BUTTON],
        [SIX_CARD_BUTTON,  SEVEN_CARD_BUTTON, EIGHT_CARD_BUTTON, NINE_CARD_BUTTON, TEN_CARD_BUTTON],
        [JACK_CARD_BUTTON, QUEEN_CARD_BUTTON, KING_CARD_BUTTON]]

    # GUI Window
    calculatorWindow = sg.Window('War Calculator', layout, finalize=True, modal=True)

    for playerNum in range(numPlayers):

        calculatorWindow["INSTR"].update(f"Player {playerNum + 1}. Enter each card to build your deck in order ({deckSize} total cards).")

        cardsSelected = 0

        while True:
            # event, values = calculatorWindow.read()

            # DEBUGGING ONLY
            for i in range(deckSize):
                calculator.addCard(playerNum, getCardFromEvent(list(eventToCardDict.keys())[random.randint(0, 11)]))
                cardsSelected += 1
            else:
                break

            if isCardEvent(event):
                # calculator.addCard(playerNum, getCardFromEvent(event))

                if cardsSelected >= deckSize:
                    break

            if event == sg.WIN_CLOSED:
                break
    else:
        # Calculate the Result of the War
        calculator.calculate()

    calculatorWindow.close()