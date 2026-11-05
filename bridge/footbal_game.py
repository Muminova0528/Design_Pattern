from game import Game


class FootballGame(Game):

    def develop(self):
        return f"Football game: {self.developer.write_code()}"