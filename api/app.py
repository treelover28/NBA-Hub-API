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
# automatically get port from Heroku
port = int(os.environ.get("PORT", 5000))
CORS(app)


# endpoint /handle-date, accept POST method
@app.route("/handle-date", methods=["POST"])
def handle_date_simulation():
    # receive date from the form in the request
    data = request.get_json()

    date = data["date"].split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    # handle request for unsupported seasons
    if year <= 2014 and month <= 9:
        return json.dumps("Season is not supported.")
    c = client()
    # return a JSON containing results for game on that date
    result = c.simulate_games_on_date(year, month, day)
    response = json.dumps(result)
    return response


@app.route("/handle-teams", methods=["POST"])
def handle_teams_simulation():
    # get data from form
    data = request.get_json()
    # get team names
    teamA = data["home"]
    teamB = data["away"]
    # convert string to int to get team season
    teamA_season = int(data["homeSeason"])
    teamB_season = int(data["awaySeason"])
    # connect to server
    c = client()
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
    response.headers.add(
        "Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept"
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
    return response


app.run(debug=True, host="0.0.0.0", port=port, threaded=True)
