### 11/28/2019
* Fixed backend endpoints:
  * ```/teams``` endpoint now contains different versions of a team from the 2014-2015 season to present.
  * Each team object in ```/teams``` endpoint now contain a list of embedded players who was/is in the team's roster for that respective season.
  * ``` /players``` endpoint created. It now has **3627 versions** of players who played/plays in the NBA from the 2014-2015 season to now.
  * Each player document keep track of the following stats:
    * Name
    * Position
    * Season
    * PER (Player Efficiency Rating)
    * TS% (True Shooting Percentage)
    * DWS (Defensive Win Shares)
    * OWS (Offensive Win Shares)
    * Points 
    * Rebounds
    * Assists
    * Offensive Rating
    * Defensive Rating
    
* Allow simulation between teams in different seasons! For example, 2015 Warriors vs 2019 Lakers! '
* Allow more dynamic searching for teams and players by using regex matching:
  * you can search for players just by typing substring of their names 
  * you can simulate games between teams without having to type the full team out! For example,
    
    ```python  
    c = client()
    # 2015 Brooklyn Nets vs 2019 Lakers
    c.simulate_game(team_a="brk", team_b="lakers", season_of_A=2015, season_of_B=2019)
    # 2015 Warriors vs 2019 Raptors
    c.simulate_game(team_a="warriors", team_b="tor", season_of_A=2015, season_of_B=2019)
    ```
 * Allow more accurate ``` simulate_games_on_date(year, month, day)``` by using season-appropriate versions of teams to simulate. 
 For example, ``` simulate_games_on_date(2016, 12, 28)``` would use the 2017-season version of teams to simulate the matchup instead
 of current 2020 version.

### 11/27/2019
* Set up backend database using MongoDB
* Added scraping functions to extract data about:
    * Team statistics
    * Game schedules 
* Added Monte Carlos simulation algorithm.
