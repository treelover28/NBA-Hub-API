## SETTINGS

# allows requests from all parties
X_DOMAINS = "*"
# connect to MongoDB server
MONGO_URI = "mongodb://localhost:27017/nba"
# allowed team names
allowed_teamName = [
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards",
]

# define team_schema
team_schema = {
    "team_name": {"type": "string", "required": True, "allowed": allowed_teamName},
    "conference": {"type": "string", "allowed": ["East", "West", "None"]},
    "wins": {"type": "integer", "min": 0, "max": 82},
    "loss": {"type": "integer", "min": 0, "max": 82},
    "offensive_rating": {"type": "float", "min": 0, "required": True},
    "defensive_rating": {"type": "float", "min": 0, "required": True},
    "pace": {"type": "float", "min": 0, "required": True},
}
# define schema of matchup endpoint
matchup_schema = {
    "date": {"type": "float", "required": True},  # will convert using datetime
    "matchup_teams": {
        "type": "list",
        "schema": {
            "type": "objectid",
            "required": True,
            "data_relation": {"resource": "teams", "embeddable": True, "field": "_id"},
            "maxlength": 2,
            "minlength": 2,
        },
    },
}
RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

DOMAIN = {"teams": {"schema": team_schema}, "matchups": {"schema": matchup_schema}}
