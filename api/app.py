from eve import Eve
import sys
from flask import request
from client import client
import pandas as pd
import os
from pathlib import Path
import json
from flask_cors import CORS

app = Eve()
CORS(app)


# endpoint /handle-date, accept POST method
@app.route("/handle-date", methods=["POST"])
def handle_date_simulation():
    # receive date from the form in the request
    date = request.form["date"].split("-")
    c = client()
    # update database
    c.update()
    # return a JSON containing results for game on that date
    result = c.simulate_games_on_date(int(date[0]), int(date[1]), int(date[2]))
    response = json.dumps(result)
    return response


@app.route("/handle-teams", methods=["POST"])
def handle_teams_simulation():
    # get data from form
    data = request.form
    # get team names
    teamA = data["teamA"]
    teamB = data["teamB"]
    # convert string to int to get team season
    teamA_season = int(data["teamA_season"])
    teamB_season = int(data["teamB_season"])
    # connect to server and update if necessary
    c = client()
    c.update()
    # get back dictionary of result
    result = c.simulate_game(
        teamA, teamB, season_of_A=teamA_season, season_of_B=teamB_season
    )
    # send back json of result to frontend
    response = json.dumps(result)
    # print(response, file=sys.stderr)
    return response


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


app.run(debug=True)
