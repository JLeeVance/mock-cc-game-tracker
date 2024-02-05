class Game:
    all_games = []

    def __init__(self, title):
        self.title = title
        self.all_results = []
        self.all_players = []
        Game.all_games.append(self)

    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, "title"):
            self._title = new_title
        else:
            raise Exception("The title must be a string and can not be changed!")

    def results(self):
        return self.all_results

    def players(self):
        uni_players = []
        for player in self.all_players:
            if player not in uni_players:
                uni_players.append(player)
        return uni_players

    def average_score(self, player):
        if isinstance(player, Player):
            avg_list = [result.score for result in self.all_results if result.player == player]
            personal_avg = sum(avg_list) / len(avg_list)
            return personal_avg
        else:
            raise Exception("The player must be of instance player.")

class Player:
    all_players = []

    def __init__(self, username):
        self.username = username
        Player.all_players.append(self)
        self.my_games = []
        self.my_results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_user):
        if isinstance(new_user, str) and len(new_user) >= 2 and len(new_user) <= 16:
            self._username = new_user
        else:
            raise Exception("The new username must be a string")

    def results(self):
        return self.my_results

    def games_played(self):
        games_played = []
        for game in self.my_games:
            if game not in games_played:
                games_played.append(game)
        return games_played
    
        
    def played_game(self, game):
        if isinstance(game, Game):
            if game in self.my_games:
                return True
            else:
                return False

    def num_times_played(self, game):
        if isinstance(game, Game):
            num_times = 0
            for result in self.my_results:
                if result.game == game:
                    num_times += 1
            return num_times
        else:
            raise Exception("The game provided must by of instance class Game")

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score

        player.my_results.append(self)
        player.my_games.append(game)

        game.all_players.append(player)
        game.all_results.append(self)

        Result.all.append(self)

    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("The player must be of instance class Player!")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception("The game must be of instance class Game")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) and new_score >= 1 and new_score <= 5000 and not hasattr(self, "score"):
            self._score = new_score
        else:
            raise Exception("The score must be an int between 1 and 5000, and can not be changed.")
    
    @classmethod
    def get_all_results(cls):
        return cls.all
