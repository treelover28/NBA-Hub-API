import sys

sys.path.append("../")
from server import server
import scraper
import simulation
import pymongo
from Team import Team
from pprint import pprint as pretty
from datetime import datetime


class client(object):
    def __init__(self):
        # connect to mongoDB
        self.my_client = pymongo.MongoClient("localhost", 27017)
        self.db = self.my_client.get_database("nba")

    def simulate_games_on_date(self, year: int, month: int, day: int):
        """
        Scrape NBA-Reference for schedule on specific date. Simulate all games on that date and print 
        simulation results to terminal
        """
        return server.simulate_all_games_on_date(server(), year, month, day)

    def simulate_game(
        self,
        team_a: str,
        team_b: str,
        repetition: int = 10000,
        season_of_A: int = 2020,
        season_of_B: int = 2020,
    ):
        """
        Return the probabilities of each team winning the matchup, the predicted scores, and the probability of them going to overtime.\n

        Arguments :
            team_a (str) : full team name, or team abbreviation, or partial string of team name of the first team. 
            \n
            team_b (str) : full team name, or team abbreviation, or partial string of team name of the second team. 
            \n
            repetition (int): how many times to repeat the simulation (by default, 10,000) to output average sample probabilities
            that will approach the real probabilities by Central Limit Theorem. 
            \n
            season_of_A (int) : which seasonal-version of team A to use for simulation. 
            \n
            season_of_B (int) : : which seasonal-version of team A to use for simulation. 
        """
        return server.simulate(
            server(), team_a, team_b, repetition, season_of_A, season_of_B
        )

    def get_all_teams(self, season: int = 2020, printData: bool = False):
        """
        Return a list of team objects that obey specified properties: \n
        Arguments:
            season (int) : season number which is 2020 (current season) by default. \n
            printData (bool) : print the returned list of teams nicely.
        """
        # get list of all teams in a current season as a JSON from MongoDB
        results = self.db["teams"].find({"season": season})
        if results is not None:
            teams = []
            for result in results:
                # if user specifies to print data then pretty-print it
                if printData:
                    pretty(result)
                # create team object and add to list
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
            return teams  # return list of teams
        # else, if teams are not found on database, return nothing
        return None

    def get_team(self, team_name: str, season: int):
        """
        Return a Team object of specified team at specified season. \n
        Arguments :

            :param team_name (str) : name of team.
            :param season (int): the seasonal version of the team.
            :rtype: Team object.
        """
        connection = server()
        return connection.get_team(team_name, season)

    def get_players(self, player_name: str, season: int):
        """
        Return a list of Player objects of matching players at specified season. \n
        Arguments :
            :param player_name (str) : name of player. Support search for partial strings of player names. \n
            :param season (int): the seasonal version of the team.

        :Example:

            A search for get_players("james", 2020) will return a list of players that has the 
            word "james" in either their last or first names in the 2020 season.
        """
        connection = server()
        return connection.get_players(player_name, season)

    # def update(self):
    #     """
    #     Update team statistics on database if last update was more than 24 hours ago. \n
    #     No argument.
    #     """
    #     team = self.db["teams"].find_one({"season": 2020})
    #     # find time differences
    #     time_diff = datetime.today() - team["_created"]
    #     # if total time difference is more than 24 hours, then update
    #     if time_diff.total_seconds() > (24 * 3600):
    #         connection = server()
    #         connection.update_teams_specified_season(2020)
    #         print("UPDATED")


def main():
    c = client()
    c.simulate_game("lac", "lal")
    c.simulate_games_on_date(2019, 12, 25)


if __name__ == "__main__":
    main()
