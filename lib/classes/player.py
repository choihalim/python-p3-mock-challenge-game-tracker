class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        if game in self._games_played:
            return True
        return False

    def num_times_played(self, game):
        return len([r for r in self._results if r.game == game])

    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            hs_player = None
            high_score = 0
            for player in cls.all:
                if game.average_score(player) > high_score:
                    hs_player = player
                    high_score = game.average_score(player)
            return hs_player
        return None
