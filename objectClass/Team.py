class Team(object):
    def __init__(
        self,
        team_name: str,
        offensive_rating: float,
        defensive_rating: float,
        pace: float,
        conference: str = None,
        wins: int = 0,
        loss: int = 0,
    ):
        self.team_name = team_name
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating
        self.pace = pace
        self.conference = conference
        self.wins = wins
        self.loss = loss

    def __str__(self):
        return "{}, off_rtg: {}, def_rtg: {}, pace: {}, wins: {}, losses: {} ".format(
            self.team_name,
            self.offensive_rating,
            self.defensive_rating,
            self.pace,
            self.wins,
            self.loss,
        )

