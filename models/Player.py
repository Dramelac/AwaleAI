from models.PlayerBase import PlayerBase


class Player(PlayerBase):

    def __init__(self):
        super().__init__()

    def choice(self):
        print("Choose between 1 to 6:", end=' ')
        while True:
            try:
                value = int(input())
                if 0 < value < 7:
                    return value-1
                else:
                    print("Incorrect value !")
            except KeyboardInterrupt:
                exit(0)
            except Exception:
                print("Not a number !")
