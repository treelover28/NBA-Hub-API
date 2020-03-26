import React from "react";
import img_calendar from "../images/calendar.jpg";
// statically import all 30 logos
import hawks from "../images/logos/hawks.png";
import celtics from "../images/logos/celtics.png";
import nets from "../images/logos/nets.png";
import hornets from "../images/logos/hornets.png";
import bulls from "../images/logos/bulls.png";
import cavs from "../images/logos/cavs.png";
import mavs from "../images/logos/mavericks.png";
import nuggets from "../images/logos/nuggets.png";
import pistons from "../images/logos/pistons.png";
import warriors from "../images/logos/warriors.png";
import rockets from "../images/logos/rockets.png";
import pacers from "../images/logos/pacers.png";
import clippers from "../images/logos/clippers.png";
import lakers from "../images/logos/lakers.png";
import grizzlies from "../images/logos/grizzlies.png";
import heats from "../images/logos/heats.png";
import bucks from "../images/logos/bucks.png";
import wolves from "../images/logos/wolves.png";
import pelicans from "../images/logos/pelicans.png";
import knicks from "../images/logos/knicks.png";
import thunders from "../images/logos/thunders.png";
import magics from "../images/logos/magics.png";
import sixers from "../images/logos/sixers.png";
import suns from "../images/logos/suns.png";
import blazers from "../images/logos/blazers.png";
import kings from "../images/logos/kings.png";
import spurs from "../images/logos/spurs.png";
import raptors from "../images/logos/raptors.png";
import jazz from "../images/logos/jazz.png";
import wizards from "../images/logos/wizards.png";

import "../styles/simulateMatchup.css";
import SimulationResult from "./SimulationResult";
import "../styles/simulationDate.css";
class SimulationDate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: "",
      result: null,
      simulated: false
    };
    // dictionary to get team logo
    this.teams = {
      "Atlanta Hawks": hawks,
      "Boston Celtics": celtics,
      "Brooklyn Nets": nets,
      "Charlotte Hornets": hornets,
      "Chicago Bulls": bulls,
      "Cleveland Cavaliers": cavs,
      "Dallas Mavericks": mavs,
      "Denver Nuggets": nuggets,
      "Detroit Pistons": pistons,
      "Golden State Warriors": warriors,
      "Houston Rockets": rockets,
      "Indiana Pacers": pacers,
      "Los Angeles Clippers": clippers,
      "Los Angeles Lakers": lakers,
      "Memphis Grizzlies": grizzlies,
      "Miami Heat": heats,
      "Milwaukee Bucks": bucks,
      "Minnesota Timberwolves": wolves,
      "New Orleans Pelicans": pelicans,
      "New York Knicks": knicks,
      "Oklahoma City Thunder": thunders,
      "Orlando Magic": magics,
      "Philadelphia 76ers": sixers,
      "Phoenix Suns": suns,
      "Portland Trail Blazers": blazers,
      "Sacramento Kings": kings,
      "San Antonio Spurs": spurs,
      "Toronto Raptors": raptors,
      "Utah Jazz": jazz,
      "Washington Wizards": wizards
    };
  }

  simulateDate = () => {
    // get form data by selecting form document
    let date = document.getElementsByClassName("date-input")[0].value;
    this.setState({ date: date });
    let data = JSON.stringify({ date: date });
    console.log(data);
    // send POST request to API endpoint/handle_date
    let xhr = new XMLHttpRequest();
    const url = "http://127.0.0.1:5000/handle-date";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    // send data
    xhr.send(data);
    xhr.onload = () => {
      let response = JSON.parse(xhr.responseText);
      this.setState({ result: response, simulated: true });
      console.log(response);
    };
  };

  render() {
    return (
      <div className="about-container decrease-top">
        <div className="about">
          <h1>SIMULATE BY DATE</h1>
          <div className="date-panel">
            <img
              src={img_calendar}
              className="img-in-box"
              alt="Lebron in front of a calendar."
            ></img>
            <div className="input-field">
              <div className="input-field-child">
                <h4>Enter a future game date you wish to simulate</h4>
                <form id="date-simulation">
                  <input
                    type="date"
                    className="date-input"
                    id="date"
                    min="2014-09-01"
                    //   max="2020-04-15"
                    required
                  />
                </form>
                <button className="button" onClick={this.simulateDate}>
                  Simulate games on Date
                </button>
              </div>
            </div>
          </div>
        </div>
        {// return result panel if there are games on the chosen date
        // else, return a message to panel notifying there are no games on that date
        this.state.simulated ? (
          this.state.result === "No game scheduled on this date." ||
          this.state.result === "Season is not supported." ? (
            <div>
              <br></br>
              <h1 className="date-info">Results on {this.state.date}</h1>
              <SimulationResult
                noGame={true}
                message={this.state.result}
              ></SimulationResult>
            </div>
          ) : (
            <div>
              <br></br>
              <h1 className="date-info">Results on {this.state.date}</h1>
              {this.state.result.map(game => {
                return (
                  <SimulationResult
                    home={game["Team A"]}
                    homeScore={game["Team A's predicted score"]}
                    homeProbs={game["Team A's chance of winning"]}
                    homeLogo={this.teams[game["Team A"]]}
                    homeSeason={game["Team A's season"]}
                    awaySeason={game["Team B's season"]}
                    away={game["Team B"]}
                    awayScore={game["Team B's predicted score"]}
                    awayProbs={game["Team B's chance of winning"]}
                    awayLogo={this.teams[game["Team B"]]}
                    overtime={game["Overtime chance"]}
                    noGame={false}
                  ></SimulationResult>
                );
              })}
            </div>
          )
        ) : null}
      </div>
    );
  }
}

export default SimulationDate;
