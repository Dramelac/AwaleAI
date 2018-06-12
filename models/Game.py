from models.AIPlayer import AIPlayer
from models.Player import Player
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
            self.playerA = AIPlayer(self.board, 1)

        # test if player 2 machine
        if confirm("Is player 2 a human ?", "N"):
            self.playerB = Player()
        else:
            self.playerB = AIPlayer(self.board, 2)

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
            self.display()
            if self.round % 2 == 0:
                print("Player 1 turn:")
                pos = self.__MiniMax()
                #pos = self.playerA.choice()
            else:
                print("Player 2 turn:")
                pos = self.playerB.choice()
                pos = (len(self.board) // 2) - pos - 1
                pos += len(self.board) // 2
            if self.__isPossible(pos):
                self.__play(pos)
                if self.get_current_player().score >= 25:
                    print("YOU WIN !")
                self.round += 1
            else:
                print("Incorrect selection")

    def __play(self, pos):
        distribute = self.board[pos]
        current_pos = pos
        self.board[pos] = 0
        for i in range(1, distribute + 1):
            # Apply point
            current_pos = (pos + i) % len(self.board)
            self.board[current_pos] += 1

        scoring = True
        while scoring:
            if self.__is_enemie_zone(current_pos) and 2 <= self.board[current_pos] <= 3:
                self.get_current_player().score += self.board[current_pos]
                self.board[current_pos] = 0
                current_pos -= 1
            else:
                scoring = False

    def get_current_player(self):
        if self.round % 2 == 0:
            # Player 1 - selecting enemies range
            return self.playerA
        else:
            # Player 2 - selecting enemies range
            return self.playerB

    def __is_enemie_zone(self, pos):
        if self.round % 2 == 0:
            # Player 1 - selecting enemies range
            return 6 <= pos < len(self.board)
        else:
            # Player 2 - selecting enemies range
            return 0 <= pos < 6

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

    def __MiniMax(self):

        save = list(self.board)
        maxScore = []
        for pos in range (0,5):
            distribute = self.board[pos]
            current_pos = pos
            self.board[pos] = 0
            for i in range(1, distribute + 1):
                # Apply point
                current_pos = (pos + i) % len(self.board)
                self.board[current_pos] += 1
            scoring = True
            while scoring:
                if self.__is_enemie_zone(current_pos) and 2 <= self.board[current_pos] <= 3:
                    maxScore.append(self.board[current_pos])
                    self.board[current_pos] = 0
                    current_pos -= 1
                else:
                    maxScore.append(0)
                    scoring = False
            self.board = list(save)

        choice = maxScore.index(max(maxScore))
        if (self.board[choice] != 0):
            return  choice
        else:
            while (choice < 6):
                choice += 1
                if (self.board[choice] != 0):
                    return choice
