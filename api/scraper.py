from bs4 import BeautifulSoup
import requests
import re
import sys

from datetime import datetime
from Team import Team
from Player import Player


def scrape_teams(season: int = 2020):
    # send a get request to basketball-reference
    # get a response object back
    nbaref = requests.get(
        "https://www.basketball-reference.com/leagues/NBA_{}_ratings.html".format(
            season
        )
    )
    # use BeautifulSoup to parse the response into XML format
    soup = BeautifulSoup(nbaref.text, "lxml")
    # lists of different statistics
    teamName = soup.findAll(attrs={"data-stat": "team_name"})
    offensive_rating = soup.findAll(attrs={"data-stat": "off_rtg"})
    defensive_rating = soup.findAll(attrs={"data-stat": "def_rtg"})
    w = soup.findAll(attrs={"data-stat": "wins"})
    l = soup.findAll(attrs={"data-stat": "losses"})

    # generate list of teams information
    teamList = []
    for i in range(1, 31):
        # group statistics together to form team
        team = Team(
            teamName[i].text,
            int(season),
            float(offensive_rating[i].text),
            float(defensive_rating[i].text),
            100.00,
            wins=int(w[i].text),
            loss=int(l[i].text),
        )
        teamList.append(team)
    # sort teamList by alphabetical order
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
    # get corresponding season back
    season = season_of_date(year, month, day)

    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games-{switch_month(month)}.html"
    schedule = requests.get(url)
    soup = BeautifulSoup(schedule.text, "lxml")

    # format of month of URL is first 3 letters with first letter capitalized
    # 11 => november => Nov
    m = switch_month(month)[0:3].capitalize()

    # NBA reference stores game using the following date format:
    # Nov 11, 2019
    date = "{} {}, {}".format(m, day, year)
    calendar = soup.findAll("tr")
    games_on_date = []

    # flag to stop searching after all games of matching date have been found
    dateFound = False
    for c in calendar:
        # use string matching to find games on with matching date
        if date in c.text:
            dateFound = True
            match = (
                c.find(attrs={"data-stat": "visitor_team_name"}).text,
                c.find(attrs={"data-stat": "home_team_name"}).text,
            )
            games_on_date.append(match)
        else:
            dateFound = False
        # after you have scraped all games on matching date, and dateFound = False and the length of list must be greater than 0
        # break out of loop
        # else, if there are still games with matching date, dateFound remain True
        if dateFound is False and len(games_on_date) > 0:
            break
    return games_on_date


def season_of_date(year: int, month: int, day: int):
    # Any game in June to December of 2019 technically belongs to the 2020 season
    if month > 6 and month <= 12:
        season = year + 1
    else:
        season = year
    return season


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
    # date format is 2019-20
    date = f"{season-1}-{str(season)[-2:]}"
    # return a tuple of pace and offensive rating
    for d in data:
        if date in d.text:
            pace = d.find(attrs={"data-stat": "pace"})
            off_rtg = d.find(attrs={"data-stat": "off_rtg"})
            return (float(pace.text), float(off_rtg.text))


def scrape_players(season: int = 2020):
    if season < 2015 and season > 2020:
        print(f"Your specified season {season} is not supported")
        return
    else:
        per_game_url = (
            f"https://www.basketball-reference.com/leagues/NBA_{season}_per_game.html"
        )
        per_pos_url = (
            f"https://www.basketball-reference.com/leagues/NBA_{season}_per_poss.html"
        )
        advanced_url = (
            f"https://www.basketball-reference.com/leagues/NBA_{season}_advanced.html"
        )
        # get data for selected statistics
        per_game_doc = requests.get(per_game_url)
        per_game_soup = BeautifulSoup(per_game_doc.text, "lxml")
        player_name = per_game_soup.findAll(attrs={"data-stat": "player"})
        position = per_game_soup.findAll(attrs={"data-stat": "pos"})
        pts = per_game_soup.findAll(attrs={"data-stat": "pts_per_g"})
        trb = per_game_soup.findAll(attrs={"data-stat": "trb_per_g"})
        ast = per_game_soup.findAll(attrs={"data-stat": "ast_per_g"})

        advanced_doc = requests.get(advanced_url)
        advanced_soup = BeautifulSoup(advanced_doc.text, "lxml")
        per = advanced_soup.findAll(attrs={"data-stat": "per"})
        ts_pct = advanced_soup.findAll(attrs={"data-stat": "ts_pct"})
        for pct in player_name:
            print(pct.text)
        ows = advanced_soup.findAll(attrs={"data-stat": "ows"})
        dws = advanced_soup.findAll(attrs={"data-stat": "dws"})

        per_poss_doc = requests.get(per_pos_url)
        per_poss_soup = BeautifulSoup(per_poss_doc.text, "lxml")
        offensive_rating = per_poss_soup.findAll(attrs={"data-stat": "off_rtg"})
        defensive_rating = per_poss_soup.findAll(attrs={"data-stat": "def_rtg"})

        playerList = []
        for i in range(1, len(player_name)):
            name = player_name[i].text
            pos = position[i].text
            # in case a stat doesn't exist, Basketball Reference stores a empty value for the stat
            # we cannot cast an empty string to a float so just change any empty string to 0
            PER = per[i].text or 0
            ts = ts_pct[i].text or 0
            DWS = dws[i].text or 0
            OWS = ows[i].text or 0
            ppg = pts[i].text or 0
            rpg = trb[i].text or 0
            apg = ast[i].text or 0
            off_rtg = offensive_rating[i].text or 0
            def_rtg = defensive_rating[i].text or 0

            # scraped content also contain text header, this is to skip unnecessary text-headers
            # PER is a numerical column, so if we encounter a text at per[i], it means our current row of data
            # is a header row!
            if per[i].text.isalpha():
                continue
            player = Player(
                name,
                pos,
                season,
                float(PER),
                float(ts),
                float(DWS),
                float(OWS),
                float(ppg),
                float(rpg),
                float(apg),
                float(off_rtg),
                float(def_rtg),
            )
            playerList.append(player)
            # print(player)
        return playerList


def switch_name_abbrev(team_name: str):
    if len(team_name) < 3:
        print("Query is too short to find exact team. Try 3 characters or more.")
        return
    lookup = {
        "Atlanta Hawks": "ATL",
        "Boston Celtics": "BOS",
        "Brooklyn Nets": "BRK",
        "Charlotte Hornets": "CHO",
        "Chicago Bulls": "CHI",
        "Cleveland Cavaliers": "CLE",
        "Dallas Mavericks": "DAL",
        "Denver Nuggets": "DEN",
        "Detroit Pistons": "DET",
        "Golden State Warriors": "GSW",
        "Houston Rockets": "HOU",
        "Indiana Pacers": "IND",
        "Los Angeles Clippers": "LAC",
        "Los Angeles Lakers": "LAL",
        "Memphis Grizzlies": "MEM",
        "Miami Heat": "MIA",
        "Milwaukee Bucks": "MIL",
        "Minnesota Timberwolves": "MIN",
        "New Orleans Pelicans": "NOP",
        "New York Knicks": "NYK",
        "Oklahoma City Thunder": "OKC",
        "Orlando Magic": "ORL",
        "Philadelphia 76ers": "PHI",
        "Phoenix Suns": "PHX",
        "Portland Trail Blazers": "POR",
        "Sacramento Kings": "SAC",
        "San Antonio Spurs": "SAS",
        "Toronto Raptors": "TOR",
        "Utah Jazz": "UTA",
        "Washington Wizards": "WAS",
    }
    # return a list of possible matches
    # we usually expect a list of one value tho!
    result = []
    for k in lookup:
        if team_name.lower() in k.lower():
            result.append(lookup[k])
    return result


def scrape_team_roster(teamName: str, season: int = 2020):
    url = f"https://www.basketball-reference.com/teams/{switch_name_abbrev(teamName)[0]}/{season}.html"
    doc = requests.get(url)
    soup = BeautifulSoup(doc.text, "lxml")
    roster = []
    players_names = soup.findAll(attrs={"data-stat": "player"})
    for p in players_names:
        # don't include "Player" headers or Two-way players
        if "(TW)" not in p.text and p.text is not "Player":
            roster.append(p.text)
    return roster


# print(soup)
