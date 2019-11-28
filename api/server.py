import pymongo
import json
import requests
from pprint import pprint as pretty
import sys
import scraper
import simulation

sys.path.append("../")
from objectClass.Team import Team


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

        if post_request.status_code != 201:
            print(
                "Error occured with post_team(). Status code: {}, \n {} ".format(
                    post_request.status_code, post_request.text
                )
            )
        else:
            print("Team posted successfully! Team : {}".format(team_data["team_name"]))

    def update_team(self):
        teamList = scraper.scrape_teams()
        self.delete_all_teams()
        for t in teamList:
            self.post_team(t)

    def get_team(self, teamName: str):
        result = self.db["teams"].find_one({"team_name": teamName})
        if result is not None:
            team = Team(
                team_name=result["team_name"],
                offensive_rating=result["offensive_rating"],
                defensive_rating=result["defensive_rating"],
                pace=result["pace"],
                wins=result["wins"],
                loss=result["loss"],
            )
            return team
        return None


def main():
    connection = server()
    # connection.delete_all_teams()
    # lal = Team("LA Lakers", "111.39", "102.76", "100", "West", 14, 2)
    # connection.post_team(lal)
    # connection.update_team()
    # scrape_teams(2020)
    # games = scraper.scrape_schedule(2018, 12, 25)
    # print(games)
    # scraper.scrape_league_pace()
    # simulation.simulate("LAL", "MIL")
    # simulation.simulateMatches(teamList[18], teamList[4])
    simulation.simulate_all_games_on_date(2019, 11, 25)


if __name__ == "__main__":
    main()
