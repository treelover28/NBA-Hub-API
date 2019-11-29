from server import server
import scraper
import simulation
import pymongo
from objectClass.Team import Team
from pprint import pprint as pretty


class client(object):
    def __init__(self):
        self.my_client = pymongo.MongoClient("localhost", 27017)
        self.db = self.my_client["nba"]

    def simulate_games_on_date(self, year: int, month: int, day: int):
        simulation.simulate_games_on_date(year, month, day)

    def simulate_game(
        self,
        team_a: str,
        team_b: str,
        repetition: int = 10000,
        season_of_A: int = 2020,
        season_of_B: int = 2020,
    ):
        simulation.simulate(team_a, team_b, repetition, season_of_A, season_of_B)

    def get_all_teams(self, season: int = 2020, printData: bool = False):
        results = self.db["teams"].find({"season": season})
        if results is not None:
            teams = []
            for result in results:
                if printData:
                    pretty(result)
                team = Team(
                    team_name=result["team_name"],
                    season=result["season"],
                    offensive_rating=result["offensive_rating"],
                    defensive_rating=result["defensive_rating"],
                    pace=result["pace"],
                    wins=result["wins"],
                    loss=result["loss"],
                )
                teams.append(team)
            return teams
        return None

    def get_team(self, teamName: str, season: int):
        connection = server()
        return connection.get_team(teamName, season)

    def get_players(self, player_name: str, season: int):
        connection = server()
        return connection.get_players(player_name, season)


def main():
    c = client()
    c.simulate_game(team_a="lal", team_b="lakers", season_of_A=2015, season_of_B=2019)


if __name__ == "__main__":
    main()
