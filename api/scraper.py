from bs4 import BeautifulSoup
import requests
import re
import sys

sys.path.append("../")
from datetime import datetime
from objectClass.Team import Team


def scrape_teams(season: int = 2020):
    nbaref = requests.get(
        "https://www.basketball-reference.com/leagues/NBA_{}_ratings.html".format(
            season
        )
    )

    soup = BeautifulSoup(nbaref.text, "lxml")
    teamName = soup.findAll(attrs={"data-stat": "team_name"})
    offensive_rating = soup.findAll(attrs={"data-stat": "off_rtg"})
    defensive_rating = soup.findAll(attrs={"data-stat": "def_rtg"})
    w = soup.findAll(attrs={"data-stat": "wins"})
    l = soup.findAll(attrs={"data-stat": "losses"})

    teamList = []
    for i in range(1, 31):
        team = Team(
            teamName[i].text,
            float(offensive_rating[i].text),
            float(defensive_rating[i].text),
            100.00,
            wins=int(w[i].text),
            loss=int(l[i].text),
        )
        teamList.append(team)

    teamList = sorted(teamList, key=lambda x: x.team_name)

    # scrape TeamRanking for PACE factor
    team_ranking_url = "https://www.teamrankings.com/nba/stat/possessions-per-game?date={}".format(
        switch_date(season)
    )
    team_ranking = requests.get(team_ranking_url)
    soup = BeautifulSoup(team_ranking.text, "lxml")
    pace = soup.findAll("td")

    index = 0
    team_pace = []
    for p in pace:
        index = index + 1
        if p.text.replace(" ", "").isalpha():
            team_pace.append((p.text, float(pace[index].text)))
    # sort by team name
    team_pace = sorted(team_pace)
    index = 0
    for p in team_pace:
        teamList[index].pace = p[1]
        index = index + 1
    # for t in teamList:
    #     print(t)
    return teamList


def switch_date(season: int = 2020):
    switch = {
        2020: datetime.today().strftime("%Y-%m-%d"),
        2019: "2019-06-14",
        2018: "2018-06-09",
        2017: "2017-06-13",
        2016: "2016-06-20",
        2015: "2015-06-16",
    }
    valid_season = switch.get(season)
    if valid_season:
        return switch[season]
    else:
        return None


def scrape_schedule(year: int, month: int, day: int):
    if month > 6 and month <= 12:
        season = year + 1
    else:
        season = year

    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games-{switch_month(month)}.html"
    schedule = requests.get(url)
    soup = BeautifulSoup(schedule.text, "lxml")

    m = switch_month(month)[0:3].capitalize()
    # print(m)

    date = "{} {}, {}".format(m, day, year)
    calendar = soup.findAll("tr")
    games_on_date = []
    for c in calendar:
        # print(c.text)
        if date in c.text:
            match = (
                c.find(attrs={"data-stat": "visitor_team_name"}).text,
                c.find(attrs={"data-stat": "home_team_name"}).text,
            )
            games_on_date.append(match)
    return games_on_date


def switch_month(month):
    switch = {
        1: "january",
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "december",
    }
    valid_month = switch.get(month)
    if valid_month:
        return switch[month]
    else:
        return None


def scrape_league_pace(season: int = 2020):
    league_avg = requests.get(
        "https://www.basketball-reference.com/leagues/NBA_stats_per_game.html"
    )
    soup = BeautifulSoup(league_avg.text, "lxml")
    data = soup.findAll("tr")
    date = f"{season-1}-{str(season)[-2:]}"
    # print(date)
    for d in data:
        if date in d.text:
            pace = d.find(attrs={"data-stat": "pace"})
            off_rtg = d.find(attrs={"data-stat": "off_rtg"})
            return (float(pace.text), float(off_rtg.text))


# print(soup)

