from models.AIPlayer import AIPlayer
from models.Player import Player
from tools.awale import awale_play
from tools.input_methods import confirm


class Game:

    def __init__(self):
        print("Welcome to AWALE !\n")
        self.board = [4] * 12
        self.round = 0

        # test if player 1 is machine
        if confirm("Is player 1 a human ?"):
            self.playerA = Player()
        else:
            self.playerA = AIPlayer(self.board, 0)

        # test if player 2 machine
        if confirm("Is player 2 a human ?", "N"):
            self.playerB = Player()
        else:
            self.playerB = AIPlayer(self.board, 1)

    def display(self):
        print(" " * 11, end='| ')
        for x in range(1, 7):
            print(x, end=" | ")
        print("\n")

        print("  Player1  ", end="| ")
        for x in range(0, len(self.board) // 2):
            print(self.board[x], end=" | ")
        print()

        print("  Player2  ", end="| ")
        for x in range(len(self.board) - 1, (len(self.board) // 2) - 1, -1):
            print(self.board[x], end=" | ")
        print("\n")
        print("   Score     PlayerA:", self.playerA.get_score(), "- PlayerB", self.playerB.get_score(), "\n")

    def start(self):
        running = True
        self.round = 0
        while running:
            print()
            self.display()
            if self.round % 2 == 0:
                print("Player 1 turn:")
                pos = self.playerA.choice()
            else:
                print("Player 2 turn:")
                pos = self.playerB.choice()
                pos = (len(self.board) // 2) - pos - 1
                pos += len(self.board) // 2
            if self.__isPossible(pos):
                score = awale_play(pos, self.board, self.round)
                self.get_current_player().score += score
                if self.get_current_player().score >= 25:
                    print("YOU WIN !")
                    return
                self.round += 1
            else:
                print("Incorrect selection")

    def get_current_player(self):
        if self.round % 2 == 0:
            # Player 1 - selecting enemies range
            return self.playerA
        else:
            # Player 2 - selecting enemies range
            return self.playerB

    def __isPossible(self, pos):
        if self.round % 2 == 1:
            if pos < len(self.board) // 2 or pos > len(self.board):
                return False
        else:
            if pos < 0 or pos > len(self.board) // 2:
                return False

        try:
            if self.board[pos] > 0:
                return True
        except IndexError:
            return False
        return False
