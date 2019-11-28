# NBA Match Predictor &copy; 
**PROJECT IN PROGRESS** 

**Author:** Khai H Lai

**Last Updated:** 11/27/2019

**Changelog:** 
* Set up backend database using MongoDB
* Added scraping functions to extract data about:
    * Team statistics
    * Game schedules 
* Added Monte Carlos simulation algorithm. 

**Language:** Python
**Technology used so far** :
* Python Eve.
* MongoDB/pyMongo driver
* BeautifulSoup scraper utilities
* To be updated

![NBA Finals 2019](https://user-images.githubusercontent.com/50902696/64215334-f46c7e80-ce4f-11e9-9d50-25ddd49c66da.jpg)
This simple program uses Monte Carlo simulation to:
 * predict the result of an NBA match.
 * output each team's probability of winning the matchup.

Also has functionality to scrape game calendar on a specified date and simulate games on that date.


### Procedure Description
The simulator uses BeautifulSoup utility to scrape data from Basketball Reference and Team Rankings. It then uses Monte-Carlo simulation (basically added random statistical variations applied on the procedure described on [Basketball Distribution](http://thebasketballdistribution.blogspot.com/2009/01/how-to-predict-final-score.html)) to give the probability of each team winning the match-up. By default, unless otherwise specified by user, the algorithm will simulate a matchup 10,000 times before returning the average winning probability for each team.

### Features to be added:
For more information and details, please refer to the [Software Requirement Specification]() for deadlines for these updates.

* Working interactive frontend/U.I
* Neural network to predict game results
* Host webapp on live website 
* Maybe user login, authentication, or email list (?)


