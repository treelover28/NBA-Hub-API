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
# define what seasons the simulator support
supported_seasons = [2015, 2016, 2017, 2018, 2019, 2020]
# define team_schema
team_schema = {
    "team_name": {"type": "string", "required": True, "allowed": allowed_teamName},
    "season": {"type": "integer", "required": True, "allowed": supported_seasons},
    "conference": {"type": "string", "allowed": ["East", "West", "None"]},
    "wins": {"type": "integer", "min": 0, "max": 82},
    "loss": {"type": "integer", "min": 0, "max": 82},
    "offensive_rating": {"type": "float", "min": 0, "required": True},
    "defensive_rating": {"type": "float", "min": 0, "required": True},
    "pace": {"type": "float", "min": 0, "required": True},
    "players": {
        "type": "list",
        "schema": {
            "type": "objectid",
            "required": True,
            "data_relation": {
                "resource": "players",
                "embeddable": True,
                "field": "_id",
            },
        },
    },
}

# define player schema and stats schema
stats_schema = {"type": "float", "required": True}

player_schema = {
    "player_name": {"type": "string", "required": True},
    "position": {
        "type": "string",
        "required": True,
        "allowed": ["PG", "SG", "SF", "PF", "C"],
    },
    "season": {"type": "integer", "required": True, "allowed": supported_seasons},
    "PER": {"type": "float", "required": True},
    "true_shooting": {"type": "float", "required": True},
    "defensive_win_shares": stats_schema,
    "offensive_win_shares": stats_schema,
    "points": stats_schema,
    "rebounds": stats_schema,
    "assists": stats_schema,
    "offensive_rating": stats_schema,
    "defensive_rating": stats_schema,
}
# define schema of matchup endpoint
# matchup_schema = {
#     "date": {"type": "float", "required": True},  # will convert using datetime
#     "matchup_teams": {
#         "type": "list",
#         "schema": {
#             "type": "objectid",
#             "required": True,
#             "data_relation": {"resource": "teams", "embeddable": True, "field": "_id"},
#             "maxlength": 2,
#             "minlength": 2,
#         },
#     },
# }
RESOURCE_METHODS = ["GET", "POST", "DELETE"]
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]

RENDERERS = ["eve.render.JSONRenderer", "eve.render.XMLRenderer"]

DOMAIN = {"teams": {"schema": team_schema}, "players": {"schema": player_schema}}
