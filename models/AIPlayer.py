from models.PlayerBase import PlayerBase
from tools.awale import awale_play


class AIPlayer(PlayerBase):
    def __init__(self, board, id):
        super().__init__()
        self.board = board
        self.id = id

    def choice(self):
        maxScore = {}
        for pos in range(6):
            if self.id > 0:
                pos_tmp = (len(self.board) // 2) - pos - 1
                pos_tmp += len(self.board) // 2
            maxScore[pos] = awale_play(pos_tmp, list(self.board), self.id)

        best_pos, best_score = -1, -1
        for pos_tmp, score in maxScore.items():
            pos_check = pos_tmp
            if self.id > 0:
                pos_check = (len(self.board) // 2) - pos_tmp - 1
                pos_check += len(self.board) // 2

            if score > best_score and self.board[pos_check] != 0:
                best_pos = pos_tmp
                best_score = score

        if best_pos == -1:
            raise NotImplementedError

        print("IA", self.id + 1, "choose", best_pos + 1)
        return best_pos
