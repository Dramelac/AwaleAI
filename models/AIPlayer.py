import random

from models.PlayerBase import PlayerBase
from tools.awale import awale_play, NoMoreOption


class AIPlayer(PlayerBase):
    def __init__(self, board, id):
        super().__init__()
        self.board = board
        self.id = id

    def choice(self):

        best_score, best_pos = self.simulate_play(list(self.board), self.id, 4)

        print("IA", self.id + 1, "choose", best_pos + 1)
        return best_pos

    def simulate_play(self, board, id, depth=1):
        # print("Simulate with", board, "for player", id)
        maxScore = self.max_score_possibilities(board, id, depth)

        # anticipate enemy strat
        # print(maxScore)
        if id != self.id:
            for key in maxScore.keys():
                maxScore[key] = maxScore[key] * -1

        best_pos, best_score = -1, None
        for pos_tmp, score in maxScore.items():
            pos_check = pos_tmp
            tmp_score = score
            tmp_best_score = best_score
            if id > 0:
                pos_check = (len(board) // 2) - pos_tmp - 1
                pos_check += len(board) // 2
            if self.id != id:
                tmp_score = abs(score)
                tmp_best_score = None if best_score is None else abs(best_score)

            if (tmp_best_score is None or tmp_score > tmp_best_score) and board[pos_check] != 0:
                best_pos = pos_tmp
                best_score = score

            elif tmp_best_score is not None and tmp_score == tmp_best_score and board[pos_check] != 0:
                if random.randint(1, 2) == 1:
                    best_pos = pos_tmp
                    best_score = score

        if best_pos == -1:
            raise NoMoreOption

        # print("Best for pl", id, ":", best_pos, "/", maxScore[best_pos])

        return best_score, best_pos

    def safe_choose(self):

        maxScore = self.max_score_possibilities(self.board, self.id)

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

    def max_score_possibilities(self, board, id, depth=1):
        maxScore = {}
        # test all input
        for pos in range(6):
            if id > 0:
                pos_tmp = (len(board) // 2) - pos - 1
                pos_tmp += len(board) // 2
            else:
                pos_tmp = pos
            tmp_board = list(board)
            maxScore[pos] = awale_play(pos_tmp, tmp_board, id)
            if depth > 1:
                # ask for recurrent responses
                maxScore[pos] += self.simulate_play(tmp_board, (id + 1) % 2, depth - 1)[0]
        return maxScore
