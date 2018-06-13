from models.AIPlayer import AIPlayer
from models.Player import Player
from tools.awale import awale_play, NoMoreOption
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
        print("   Score   Player1:", self.playerA.get_score(), "- Player2:", self.playerB.get_score(), "\n")

    def start(self):
        running = True
        self.round = 0
        print()
        self.display()
        while running:
            safe_mode = False

            try:
                if self.round % 2 == 0:
                    print("Player 1 turn:")
                    if sum(self.board[6:]) == 0:
                        pos = self.playerA.safe_choose()
                        safe_mode = True
                    elif sum(self.board[:6]) == 0:
                        self.playerB.score += sum(self.board[6:])
                        self.final()
                        return
                    else:
                        pos = self.playerA.choice()
                else:
                    print("Player 2 turn:")
                    if sum(self.board[:6]) == 0:
                        pos = self.playerB.safe_choose()
                        safe_mode = True
                    elif sum(self.board[6:]) == 0:
                        self.playerA.score += sum(self.board[:6])
                        self.final()
                        return
                    else:
                        pos = self.playerB.choice()
                    pos = (len(self.board) // 2) - pos - 1
                    pos += len(self.board) // 2
            except NoMoreOption:
                self.final()
                return

            if (safe_mode and self.__is_safe_possible(pos)) or \
                    (not safe_mode and self.__isPossible(pos)):
                score = awale_play(pos, self.board, self.round)
                self.get_current_player().score += score

                print()
                self.display()

                if self.get_current_player().score >= 25 or sum(self.board) <= 3:
                    self.final()
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

    def __is_safe_possible(self, pos):
        return self.__isPossible(pos) and (pos%6)+self.board[pos] >= 6
        # check_enemy_zone(pos + self.board[pos] % len(self.board), self.round)

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

    def final(self):
        print("\nGame Over !")
        self.recalculscore()
        if self.playerA.score > self.playerB.score:
            print("Player 1 WIN !")
        elif self.playerA.score < self.playerB.score:
            print("Player 2 WIN !")
        else:
            print("EGALITE")

    def recalculscore(self):
        for case in range(0, 6):
            if self.playerA.board[case] != 0:
                self.playerA.score += self.playerA.board[case]

        for case in range(6, 12):
            if self.playerB.board[case] != 0:
                self.playerB.score += self.playerB.board[case]
