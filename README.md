# NBA Match Predictor &copy; 
**PROJECT IN PROGRESS** 

**Author:** Khai H Lai

**Last Updated:** 11/28/2019

**Changelog**: Please refer to [changelog.md](https://github.com/treelover28/NBA-match-predictor/blob/master/changelog.md) for full history of changes. Most recent changes includes:
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
  * Allow more accurate ``` simulate_games_on_date(year, month, day)``` by using season-appropriate versions of teams to simulate. For example, ``` simulate_games_on_date(2016, 12, 28)``` would use the 2017-season version of teams to simulate the matchup instead of current 2020 version.

**Language:** Python

**Technology used so far** :
* Python Eve.
* MongoDB/pyMongo driver
* BeautifulSoup scraper utilities
* To be updated

![Lakers](https://cdn.vox-cdn.com/thumbor/bSTk8WcbM2GtJttReLLsHnudFqg=/0x0:4962x3308/1200x800/filters:focal(1577x516:2369x1308)/cdn.vox-cdn.com/uploads/chorus_image/image/65753143/1189031820.jpg.0.jpg)
This simple program uses Monte Carlo simulation to:
 * predict the result of an NBA match.
 * output each team's probability of winning the matchup.

* Has functionality to scrape game calendar on a specified date and simulate games on that date.
* Allows matchup simulation between teams from different seasons. Only support from the 2015-2020 seasons as of right now.

 
### Example simulation results on games on Christmas Day! 
![image](https://user-images.githubusercontent.com/50902696/69781254-c5258f00-116a-11ea-8a75-5226030a4498.png)

### Procedure Description
The simulator uses BeautifulSoup utility to scrape data from Basketball Reference and Team Rankings. It then uses Monte-Carlo simulation (basically added random statistical variations applied on the procedure described on [Basketball Distribution](http://thebasketballdistribution.blogspot.com/2009/01/how-to-predict-final-score.html)) to give the probability of each team winning the match-up. By default, unless otherwise specified by user, the algorithm will simulate a matchup 10,000 times before returning the average winning probability for each team.

### Features to be added:
For more information and details, please refer to the [Software Requirement Specification](https://github.com/treelover28/NBA-match-predictor/blob/master/Software%20Requirement%20Specification.md) for deadlines for these updates.

* Working interactive frontend/U.I
* Neural network to predict game results
* Host webapp on live website 
* Maybe user login, authentication, or email list (?)


