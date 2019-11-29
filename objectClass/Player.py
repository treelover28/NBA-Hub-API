class Player(object):
    def __init__(
        self,
        player_name: str,
        position: str,
        season: int,
        per: float,
        true_shooting: float,
        defensive_win_shares: float,
        offensive_win_shares: float,
        points: float,
        rebounds: float,
        assists: float,
        offensive_rating: float,
        defensive_rating: float,
    ):
        self.player_name = player_name
        self.position = position
        self.season = season
        self.per = per
        self.true_shooting = true_shooting
        self.defensive_win_shares = defensive_win_shares
        self.offensive_win_shares = offensive_win_shares
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating

    def __str__(self):
        return f"{self.player_name}, {self.position}, {self.season}"

