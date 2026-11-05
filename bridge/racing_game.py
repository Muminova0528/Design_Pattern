from game import Game


class RacingGame(Game):

    def develop(self):
        return f"Racing game: {self.developer.write_code()}"