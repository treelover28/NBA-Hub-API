import React from "react";

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

class SimulateMatchup extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      home: "Atlanta Hawks",
      away: "Boston Celtics",
      homeFinal: "Atlanta Hawks",
      awayFinal: "Boston Celtics",
      homeSeason: 2020,
      awaySeason: 2020,
      homeSeasonFinal: 2020,
      awaySeasonFinal: 2020,
      homeScore: "",
      homeProbs: "",
      awayScore: "",
      awayProbs: "",
      overtime: "",
      homePicture: hawks,
      awayPicture: celtics,
      homePictureFinal: hawks,
      awayPictureFinal: celtics,
      homeIndex: 0,
      awayIndex: 1,
      simulated: false
    };

    this.teams = [
      { team: "Atlanta Hawks", pic: hawks },
      { team: "Boston Celtics", pic: celtics },
      { team: "Brooklyn Nets", pic: nets },
      { team: "Charlotte Hornets", pic: hornets },
      { team: "Chicago Bulls", pic: bulls },
      { team: "Cleveland Cavaliers", pic: cavs },
      { team: "Dallas Mavericks", pic: mavs },
      { team: "Denver Nuggets", pic: nuggets },
      { team: "Detroit Pistons", pic: pistons },
      { team: "Golden State Warriors", pic: warriors },
      { team: "Houston Rockets", pic: rockets },
      { team: "Indiana Pacers", pic: pacers },
      { team: "Los Angeles Clippers", pic: clippers },
      { team: "Los Angeles Lakers", pic: lakers },
      { team: "Memphis Grizzlies", pic: grizzlies },
      { team: "Miami Heat", pic: heats },
      { team: "Milwaukee Bucks", pic: bucks },
      { team: "Minnesota Timberwolves", pic: wolves },
      { team: "New Orleans Pelicans", pic: pelicans },
      { team: "New York Knicks", pic: knicks },
      { team: "Oklahoma City Thunder", pic: thunders },
      { team: "Orlando Magic", pic: magics },
      { team: "Philadelphia 76ers", pic: sixers },
      { team: "Phoenix Suns", pic: suns },
      { team: "Portland Trail Blazers", pic: blazers },
      { team: "Sacramento Kings", pic: kings },
      { team: "San Antonio Spurs", pic: spurs },
      { team: "Toronto Raptors", pic: raptors },
      { team: "Utah Jazz", pic: jazz },
      { team: "Washington Wizards", pic: wizards }
    ];
  }

  getTeam(index) {
    return this.teams[index];
  }
  rightArrow = home => {
    if (home) {
      let newIndex =
        this.state.homeIndex + 1 >= 30 ? 0 : this.state.homeIndex + 1;
      let teamObj = this.getTeam(newIndex);

      this.setState({
        homeIndex: newIndex,
        home: teamObj.team,
        homePicture: teamObj.pic
      });
    } else {
      let newIndex =
        this.state.awayIndex + 1 >= 30 ? 0 : this.state.awayIndex + 1;
      let teamObj = this.getTeam(newIndex);

      this.setState({
        awayIndex: newIndex,
        away: teamObj.team,
        awayPicture: teamObj.pic
      });
    }
  };

  leftArrow = home => {
    if (home) {
      let newIndex =
        this.state.homeIndex - 1 < 0 ? 29 : this.state.homeIndex - 1;
      let teamObj = this.getTeam(newIndex);

      this.setState({
        homeIndex: newIndex,
        home: teamObj.team,
        homePicture: teamObj.pic
      });
    } else {
      let newIndex =
        this.state.awayIndex - 1 < 0 ? 29 : this.state.awayIndex - 1;
      let teamObj = this.getTeam(newIndex);

      this.setState({
        awayIndex: newIndex,
        away: teamObj.team,
        awayPicture: teamObj.pic
      });
    }
  };

  setSeason = (e, home) => {
    if (home) {
      this.setState({ homeSeason: e.target.value });
    } else {
      this.setState({ awaySeason: e.target.value });
    }
  };

  simulate = () => {
    this.setState({ simulated: true });
    // convert matchup state to data
    let rawData = {
      home: this.state.home,
      away: this.state.away,
      homeSeason: this.state.homeSeason,
      awaySeason: this.state.awaySeason
    };
    let data = JSON.stringify(rawData);
    // create XHR object
    let xhr = new XMLHttpRequest();
    const url = "http://127.0.0.1:5000/handle-teams";
    // open a POST request to url
    // async = true
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    // send data to API
    xhr.send(data);
    // get response back from API
    xhr.onload = () => {
      let response = JSON.parse(xhr.responseText);
      this.setState({
        homeFinal: response["Team A"],
        awayFinal: response["Team B"],
        homeSeasonFinal: response["Team A's season"],
        awaySeasonFinal: response["Team B's season"],
        homePictureFinal: this.state.homePicture,
        awayPictureFinal: this.state.awayPicture,
        homeProbs: response["Team A's chance of winning"],
        awayProbs: response["Team B's chance of winning"],
        homeScore: response["Team A's predicted score"],
        awayScore: response["Team B's predicted score"],
        overtime: response["Overtime chance"]
      });
      // console.log(response);
    };
  };
  render() {
    return (
      <div className="about-container center border">
        <div className="team-select">
          <div className="selection">
            <button
              className="button in-selection prev"
              onClick={this.leftArrow.bind(this, true)}
            >
              <span>Previous</span>
            </button>
            <div className="team-panel">
              <h1>HOME</h1>

              <img className="team-logo" src={this.state.homePicture}></img>

              <h3>{this.state.home}</h3>
              <h2>Season</h2>
              <select
                name="home-season"
                id="home-season"
                onChange={e => {
                  this.setSeason(e, true);
                }}
                className="button dropdown"
                required
              >
                <option value={2015}>2015</option>
                <option value={2016}>2016</option>
                <option value={2017}>2017</option>
                <option value={2018}>2018</option>
                <option value={2019}>2019</option>
                <option value={2020} selected>
                  2020
                </option>
              </select>
            </div>
            <button
              className="button in-selection next"
              onClick={this.rightArrow.bind(this, true)}
            >
              <span>Next</span>
            </button>
          </div>
          <br></br>
          <div className="selection">
            <button
              className="button in-selection prev"
              onClick={this.leftArrow.bind(this, false)}
            >
              <span>Previous</span>
            </button>
            <div className="team-panel">
              <h1>AWAY</h1>
              <img className="team-logo" src={this.state.awayPicture}></img>
              <h3>{this.state.away}</h3>
              <h2>Season</h2>
              <select
                name="away-season"
                id="away-season"
                onChange={e => {
                  this.setSeason(e, false);
                }}
                className="button dropdown"
                required
              >
                <option value={2015}>2015</option>
                <option value={2016}>2016</option>
                <option value={2017}>2017</option>
                <option value={2018}>2018</option>
                <option value={2019}>2019</option>
                <option value={2020} selected>
                  2020
                </option>
              </select>
            </div>
            <button
              className="button in-selection next"
              onClick={this.rightArrow.bind(this, false)}
            >
              <span>Next</span>
            </button>
          </div>
        </div>
        <button className="button simulate" onClick={this.simulate}>
          Simulate Matchup
        </button>
        {this.state.simulated ? (
          <SimulationResult
            home={this.state.homeFinal}
            homeScore={this.state.homeScore}
            homeProbs={this.state.homeProbs}
            homeLogo={this.state.homePictureFinal}
            homeSeason={this.state.homeSeasonFinal}
            awaySeason={this.state.awaySeasonFinal}
            away={this.state.awayFinal}
            awayScore={this.state.awayScore}
            awayProbs={this.state.awayProbs}
            awayLogo={this.state.awayPictureFinal}
            overtime={this.state.overtime}
          ></SimulationResult>
        ) : null}
      </div>
    );
  }
}

export default SimulateMatchup;
