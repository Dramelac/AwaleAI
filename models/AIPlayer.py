from models.PlayerBase import PlayerBase


class AIPlayer(PlayerBase):
    def __init__(self, board, id):
        super().__init__()
        self.board = board
        self.id = id

    def choice(self):
        print(self.board)
