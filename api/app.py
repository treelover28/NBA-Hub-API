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


@app.route("/handle_date", methods=["POST"])
def handle_date_simulation():
    date = request.form["date"].split("-")
    c = client()
    c.update()
    result = c.simulate_games_on_date(int(date[0]), int(date[1]), int(date[2]))
    response = json.dumps(result)
    return response


@app.route("/handle_teams", methods=["POST"])
def handle_teams_simulation():
    # get data from form
    data = request.form

    teamA = data["teamA"]
    teamA_season = int(data["teamA_season"])
    teamB = data["teamB"]
    teamB_season = int(data["teamB_season"])
    # print(teamA, file=sys.stderr)
    c = client()
    c.update()
    result = c.simulate_game(
        teamA, teamB, season_of_A=teamA_season, season_of_B=teamB_season
    )
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

