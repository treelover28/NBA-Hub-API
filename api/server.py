import pymongo
import json
import requests
from pprint import pprint as pretty
import sys
import scraper
import simulation
import re

sys.path.append("../")
from objectClass.Team import Team
from objectClass.Player import Player


class server(object):
    def __init__(self):
        self.my_server = pymongo.MongoClient("localhost", 27017)
        self.db = self.my_server["nba"]

    def url_for(self, endpoint):
        """
        Establish connection to particular endpoint in API
        Argument:
            endpoint (str) : name of endpoint
        Return url to endpoint
        """
        return "http://localhost:5000/{}/".format(endpoint)

    def delete_all_teams(self):
        """ 
        Void method. 
        Argument:
            No argument.
        Delete all tasks in current 'task' endpoint. \\
        Return 204 if successful. \\
        Return error code if URL is invalid or endpoint is already empty
        """
        delete_request = requests.delete(self.url_for("teams"))
        # if deletion is unsuccesful return error code
        if delete_request.status_code != 204:
            print(
                "Error occured with delete_all_teams(). Server response:",
                delete_request.status_code,
                ... and "\nEither URL is invalid or enpoint is already empty.",
            )
        else:
            print(
                "All teams have been removed. Server response: ",
                delete_request.status_code,
            )

    def post_team(self, team: Team):
        team_data = {
            "team_name": team.team_name,
            "season": team.season,
            "offensive_rating": team.offensive_rating,
            "defensive_rating": team.defensive_rating,
            "pace": team.pace,
            "conference": "None",
            "wins": 0,
            "loss": 0,
        }
        if team.conference is not None:
            team_data["conference"] = team.conference
        if team.wins is not 0:
            team_data["wins"] = team.wins
        if team.loss is not 0:
            team_data["loss"] = team.loss

        post_request = requests.post(
            self.url_for("teams"),
            json.dumps(team_data),
            headers={"Content-Type": "application/json"},
        )

        team_roster = scraper.scrape_team_roster(team.team_name, team.season)
        # roster = []
        for player in team_roster:
            # TEMPORARY SOLUTION
            # since there could be multiple versions of a players in the same season if he gets traded to different teams
            # we find all versions and add to the team
            players_to_be_embedded = self.db["players"].find(
                {"player_name": player, "season": team.season}
            )

            if players_to_be_embedded is not None:
                for p in players_to_be_embedded:
                    # print(p["_id"])
                    self.db["teams"].update_one(
                        {"team_name": team.team_name, "season": team.season},
                        {"$push": {"players": p["_id"]}},
                    )
                    # roster.append(p["_id"])

        # team_data["players"]: roster

        if post_request.status_code != 201:
            print(
                "Error occured with post_team(). Status code: {}, \n {} ".format(
                    post_request.status_code, post_request.text
                )
            )
        else:
            print("Team posted successfully! Team : {}".format(team_data["team_name"]))

    def update_teams_all_seasons(self):
        self.delete_all_teams()
        for season in range(2015, 2021):
            print(f"Updating for season {season}")
            teamList = scraper.scrape_teams(season)
            for t in teamList:
                self.post_team(t)

    def update_teams_specified_season(self, season: int = 2020):
        # delete all players in current season 2019:
        self.db["teams"].delete_many({"season": season})
        # scrape new players info in specified season
        teams = scraper.scrape_teams(season)
        for t in teams:
            self.post_team(t)

    def get_team(self, teamName: str, season: int):
        name = re.compile(teamName, re.IGNORECASE)
        result = self.db["teams"].find_one({"team_name": name, "season": season})
        if result is not None:
            team = Team(
                team_name=result["team_name"],
                season=result["season"],
                offensive_rating=result["offensive_rating"],
                defensive_rating=result["defensive_rating"],
                pace=result["pace"],
                wins=result["wins"],
                loss=result["loss"],
            )
            return team
        return None

    def post_player(self, player: Player):
        player_data = {
            "player_name": player.player_name,
            "position": player.position,
            "season": player.season,
            "PER": player.per,
            "true_shooting": player.true_shooting,
            "defensive_win_shares": player.defensive_win_shares,
            "offensive_win_shares": player.offensive_win_shares,
            "points": player.points,
            "rebounds": player.rebounds,
            "assists": player.assists,
            "offensive_rating": player.offensive_rating,
            "defensive_rating": player.defensive_rating,
        }

        post_request = requests.post(
            self.url_for("players"),
            json.dumps(player_data),
            headers={"Content-Type": "application/json"},
        )

        if post_request.status_code != 201:
            print(
                "Error occured with post_player(). Status code: {}, \n {} ".format(
                    post_request.status_code, post_request.text
                )
            )
        else:
            print(
                "Player posted successfully! Player : {} ".format(
                    player_data["player_name"]
                )
            )

    def delete_all_players_seasons(self):
        delete_request = requests.delete(self.url_for("players"))
        # if deletion is unsuccesful return error code
        if delete_request.status_code != 204:
            print(
                "Error occured with delete_all_players_seasons(). Server response:",
                delete_request.status_code,
                ... and "\nEither URL is invalid or enpoint is already empty.",
            )
        else:
            print(
                "All players and their versions have been removed. Server response: ",
                delete_request.status_code,
            )

    def update_all_players_all_seasons(self):
        # delete all players in endpoint and re-update every players
        # costly, since perform unncessary updates on past players whose stats stay the same no matter what
        self.delete_all_players_seasons()
        for i in range(2015, 2021):
            print(f"Updating for season {i}")
            playerList = scraper.scrape_players(i)
            for player in playerList:
                self.post_player(player)

    def update_all_players_specified_season(self, season: int = 2020):
        # delete all players in current season 2019:
        self.db["players"].delete_many({"season": season})
        # scrape new players info in specified season
        players = scraper.scrape_players(season)
        for player in players:
            self.post_player(player)

    def get_players(self, player_name: str, season: int):

        # support search for partial strings
        # for example, if you search for "Antetokounmpo", it would return all 3 players with that last name!
        name = re.compile(player_name, re.IGNORECASE)
        players = self.db["players"].find({"player_name": name, "season": season})

        if players is not None:
            players_matched = []
            # since there could be multiple versions of a player in a single season.
            # happens when he gets traded
            for result in players:
                pretty(result)
                player = Player(
                    player_name=result["player_name"],
                    position=result["position"],
                    season=result["season"],
                    per=result["PER"],
                    true_shooting=result["true_shooting"],
                    defensive_win_shares=result["defensive_win_shares"],
                    offensive_win_shares=result["offensive_win_shares"],
                    points=result["points"],
                    rebounds=result["rebounds"],
                    assists=result["assists"],
                    offensive_rating=result["offensive_rating"],
                    defensive_rating=result["defensive_rating"],
                )
                players_matched.append(player)
            return players_matched
        return None

