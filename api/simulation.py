from Team import Team
from numpy import random
import scraper
import datetime


def simulateMatch(a: Team, b: Team, league_avg: tuple, overtime: bool = False):
    # random [-5%, 5%] variation in offensive and defensive efficiencies
    off_rtg_A = a.offensive_rating * (1 + random.uniform(-0.05, 0.05))
    def_rtg_A = a.defensive_rating * (1 + random.uniform(-0.05, 0.05))

    off_rtg_B = b.offensive_rating * (1 + random.uniform(-0.05, 0.05))
    def_rtg_B = b.defensive_rating * (1 + random.uniform(-0.05, 0.05))

    # multiply teams' paces and divide by league_avg to find predicted game pace

    league_pace = league_avg[0]
    league_off_rtg = league_avg[1]
    gamePace = (a.pace * b.pace) / league_pace

    # for each team,
    # multiply their off_rtg with opponent's def_rtg and divide by league's average off_rtg
    # to get by-product EPPP (Exaggerated Points Per Possession)
    pppA = (off_rtg_A * def_rtg_B) / league_off_rtg
    pppB = (off_rtg_B * def_rtg_A) / league_off_rtg

    # multiply EPPP by predicted game pace, and divide by 100 to get final score
    pointA = int((pppA * gamePace) / 100)
    pointB = int((pppB * gamePace) / 100)

    if pointA == pointB:
        # if points are equal, resimulate match
        return simulateMatch(a, b, league_avg, True)
    return [(a.team_name, pointA), (b.team_name, pointB), overtime]


def simulateMatches(a: Team, b: Team, repetition: int = 10000, season: int = 2020):
    # by defailt, simulate 10,000 times
    scoreA = 0
    scoreB = 0
    winsA = 0
    winsB = 0
    overtime_count = 0
    league_avg = scraper.scrape_league_pace(season)
    # print("Simulating ...")
    for i in range(0, repetition):
        # if i % 100 == 0:
        #     print("Simulating ...")

        result = simulateMatch(a, b, league_avg)
        A_result = result[0]
        B_result = result[1]
        if A_result[1] > B_result[1]:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        if result[2] == True:
            overtime_count = overtime_count + 1

        scoreA = scoreA + A_result[1]
        scoreB = scoreB + B_result[1]

    probability_A = winsA / repetition
    probability_B = 1 - probability_A

    game_dict = {
        "Team A": a.team_name,
        "Team A's season": a.season,
        "Team A's chance of winning": str(round(probability_A * 100, 2)) + "%",
        "Team A's predicted score": str(round(scoreA / repetition, 2)) + " points",
        "Team B": b.team_name,
        "Team B's season": b.season,
        "Team B's chance of winning": str(round(probability_B * 100, 2)) + "%",
        "Team B's predicted score": str(round(scoreB / repetition, 2)) + " points",
        "Overtime chance": str(round(overtime_count / repetition * 100, 2)) + "%",
    }
    print(
        f"{a.team_name}, {a.season}: chance of winning = {round(probability_A * 100, 2)}%, predicted score = {round(scoreA/repetition,2)} \n{b.team_name}, {b.season}: chance of winning = {round(probability_B* 100,2)}%, predicted score = {round(scoreB/repetition,2)} \nChance of going to overtime : {round(overtime_count/repetition * 100,2)}% \n"
    )
    return game_dict


def is_validate_date(year: int, month: int, day: int):
    is_valid_date = True
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        is_valid_date = False
    return is_valid_date


def switch_abbreviation_teamName(team: str):
    lookup = {
        "atl": "Atlanta Hawks",
        "bos": "Boston Celtics",
        "brk": "Brooklyn Nets",
        "cho": "Charlotte Hornets",
        "chi": "Chicago Bulls",
        "cle": "Cleveland Cavaliers",
        "dal": "Dallas Mavericks",
        "den": "Denver Nuggets",
        "det": "Detroit Pistons",
        "gsw": "Golden State Warriors",
        "hou": "Houston Rockets",
        "ind": "Indiana Pacers",
        "lac": "Los Angeles Clippers",
        "lal": "Los Angeles Lakers",
        "mem": "Memphis Grizzlies",
        "mia": "Miami Heat",
        "mil": "Milwaukee Bucks",
        "min": "Minnesota Timberwolves",
        "nop": "New Orleans Pelicans",
        "nyk": "New York Knicks",
        "okc": "Oklahoma City Thunder",
        "orl": "Orlando Magic",
        "phi": "Philadelphia 76ers",
        "phx": "Phoenix Suns",
        "por": "Portland Trail Blazers",
        "sac": "Sacramento Kings",
        "sas": "San Antonio Spurs",
        "tor": "Toronto Raptors",
        "uta": "Utah Jazz",
        "was": "Washington Wizards",
    }
    valid_team = lookup.get(team)
    if valid_team:
        return lookup[team]
    else:
        return None
