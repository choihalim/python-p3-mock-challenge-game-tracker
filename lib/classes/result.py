class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

        game.results(self)
        game.players(player)

        player.results(self)
        player.games_played(game)
