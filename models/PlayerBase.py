class PlayerBase:

    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def choice(self):
        raise NotImplementedError

    def safe_choose(self):
        raise NotImplementedError
