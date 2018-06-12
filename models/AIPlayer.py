from models.PlayerBase import PlayerBase
from tools.awale import awale_play, NoMoreOption


class AIPlayer(PlayerBase):
    def __init__(self, board, id):
        super().__init__()
        self.board = board
        self.id = id

    def choice(self):

        maxScore = self.max_score_possibilities()

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
            raise NoMoreOption

        print("IA", self.id + 1, "choose", best_pos + 1)
        return best_pos

    def safe_choose(self):

        maxScore = self.max_score_possibilities()

        best_pos, best_score, best_safe = -1, -1, 20
        for pos_tmp, score in maxScore.items():
            pos_check = pos_tmp
            if self.id > 0:
                pos_check = (len(self.board) // 2) - pos_tmp - 1
                pos_check += len(self.board) // 2

            if self.board[pos_check] != 0:
                tmp_safe = self.board[pos_check] + (pos_check % 6)
                if (best_safe > tmp_safe >= 6) or (best_safe == tmp_safe and score > best_score):
                    best_pos = pos_tmp
                    best_score = score
                    best_safe = tmp_safe

        if best_pos == -1:
            raise NoMoreOption

        print("IA", self.id + 1, "choose", best_pos + 1)
        return best_pos

    def max_score_possibilities(self):
        maxScore = {}
        for pos in range(6):
            if self.id > 0:
                pos_tmp = (len(self.board) // 2) - pos - 1
                pos_tmp += len(self.board) // 2
            else:
                pos_tmp = pos
            maxScore[pos] = awale_play(pos_tmp, list(self.board), self.id)
        return maxScore
