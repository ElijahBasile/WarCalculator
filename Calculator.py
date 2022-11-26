# Base Logic for Calculating War Result

from collections import deque

from Card import *

class Calculator:
    """Calculator Class containing methods for determining the war result
    """

    def __init__(self, numPlayers : int):
        """Constructor
        """
        self.numPlayers = numPlayers
        self.playerDecks = dict()
        for num in range(numPlayers):
            self.playerDecks[num] = deque()

    def addCard(self, playerNum : int, card : Card):
        """Add card to dictionary for calculation

        Args:
            playerNum (int): Player Index
            card (Card): Card to add
        """
        self.playerDecks[playerNum].append(card)

    def calculate(self, verbose = True):
        """Calculate the War Result
        """

        playersAtWar = [] # Players that are tied and engaged in war
        pot = [] # Contains all cards in the pot
        atWar = False

        playerStatuses = [1] * self.numPlayers

        while True:
            winningPlayerNum = -1
            winningRank = -1
            for playerNum in range(self.numPlayers):

                if self.playerDecks[playerNum]:
                    # Initial Player
                    if winningPlayerNum == -1:
                        winningPlayerNum = playerNum
                        card = self.playerDecks[playerNum][0]
                        pot.append(card)
                        winningRank = card.getRank()

                        if verbose:
                            print(self.playerDecks[playerNum][0].getRank(), end =" ")

                        self.playerDecks[playerNum].popleft() # Remove card from pile

                    # Remaining Players
                    else:
                        currPlayerCard = self.playerDecks[playerNum][0]
                        pot.append(currPlayerCard)

                        if verbose:
                            print(currPlayerCard.getRank(), end =" ")

                        # Current Card outranks winning card
                        if winningRank < currPlayerCard.getRank():
                            winningPlayerNum = playerNum
                            winningRank = currPlayerCard.getRank()
                            atWar = False
                            playersAtWar.clear()

                        # Current card ties winning card
                        elif winningRank == currPlayerCard.getRank():
                            # War!!
                            atWar = True
                            if not playersAtWar:
                                playersAtWar.append(winningPlayerNum)
                            playersAtWar.append(playerNum)

                        self.playerDecks[playerNum].popleft() # Remove card from pile
                else:
                    playerStatuses[playerNum] = 0

            # If in war, each player adds 3 cards to pot, and judges the fourth card
            if atWar:
                winningPlayerNum = self.war(playersAtWar, pot, playerStatuses, verbose)
                atWar = False
                playersAtWar.clear()

            print(f" - Winner: {winningPlayerNum}")

            # Add all cards in pot to winning player's hand
            for potCard in pot:
                self.playerDecks[winningPlayerNum].append(potCard)

            if sum(playerStatuses) == 1:
                print(f"PLAYER {playerStatuses.index(1)} WINS")
                break

            pot.clear()


    def war(self, playersAtWar : list, pot : list, playerStatuses : list, verbose = False):
        """War (Recursive if needed)

        Args:
            playersAtWar (list): Players at War
            pot (list): Cards in Pot
        """

        if verbose:
            print(f" - WAR: {playersAtWar}", end = " ")

        winningWarPlayer = -1
        winningWarRank = -1
        newPlayersAtWar = []
        atWar = False
        for playerAtWar in playersAtWar:
            print(f"\n   Hidden ({playerAtWar}):", end = " ")
            if len(self.playerDecks[playerAtWar]) >= 4:
                for i in range(3):
                    print(self.playerDecks[playerAtWar][0].getRank(), end = ",")
                    pot.append(self.playerDecks[playerAtWar][0])
                    self.playerDecks[playerAtWar].popleft()

                currWarCard = self.playerDecks[playerAtWar][0]
                pot.append(currWarCard)

                print(f"\n    Active: {currWarCard.getRank()}")

                # Initial condition
                if winningWarPlayer == -1:
                    winningWarPlayer = playerAtWar
                    winningWarRank = currWarCard.getRank()

                # Remaining players
                elif winningWarRank < currWarCard.getRank():
                    winningWarPlayer = playerAtWar
                    winningWarRank = currWarCard.getRank()
                    atWar = False
                    newPlayersAtWar.clear()

                elif winningWarRank == currWarCard.getRank():
                    # War!! ... again
                    atWar = True
                    print("MATCH")
                    if not newPlayersAtWar:
                        newPlayersAtWar.append(winningWarPlayer)
                    newPlayersAtWar.append(playerAtWar)

                self.playerDecks[playerAtWar].popleft()
            else:
                for i in range(len(self.playerDecks[playerAtWar])):
                    print(self.playerDecks[playerAtWar][0].getRank(), end = ",")
                    pot.append(self.playerDecks[playerAtWar][0])
                    self.playerDecks[playerAtWar].popleft()
                playerStatuses[playerAtWar] = 0

        # If in war... again, each player adds 3 cards to pot, and judges the fourth card
        print(newPlayersAtWar)
        if atWar:
            return self.war(newPlayersAtWar, pot, playerStatuses, verbose)
        else:
            return winningWarPlayer