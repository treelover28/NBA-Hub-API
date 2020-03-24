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
      homeSeason: 2020,
      awaySeason: 2020,
      homePicture: hawks,
      awayPicture: celtics,
      homeIndex: 0,
      awayIndex: 1,
      simulated: false
    };

    this.teams = [
      { team: "Atlanta Hawks", pic: hawks },
      { team: "Boston Celtics", pic: celtics },
      { team: "Brookyn Nets", pic: nets },
      { team: "Charlotte Hornets", pic: hornets },
      { team: "Chicago Bulls", pic: bulls },
      { team: "Cleveland Cavaliers", pic: cavs },
      { team: "Dallas Mavericks", pic: mavs },
      { team: "Denver Nuggets", pic: nuggets },
      { team: "Detroit Pistons", pic: pistons },
      { team: "Golden State Warriors", pic: warriors },
      { team: "Houton Rockets", pic: rockets },
      { team: "Indiana Pacers", pic: pacers },
      { team: "Los Angeles Clippers", pic: clippers },
      { team: "Los Angeles Lakers", pic: lakers },
      { team: "Memphis Grizzlies", pic: grizzlies },
      { team: "Miami Heats", pic: heats },
      { team: "Milwaukee Bucks", pic: bucks },
      { team: "Minnesota Timberwolves", pic: wolves },
      { team: "New Orleans Pelicans", pic: pelicans },
      { team: "New York Knicks", pic: knicks },
      { team: "Oklahoma City Thunders", pic: thunders },
      { team: "Orlando Magics", pic: magics },
      { team: "Philadelphia Sixers", pic: sixers },
      { team: "Phoenix Suns", pic: suns },
      { team: "Portland Trailblazers", pic: blazers },
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
    alert("Simulate");
    this.setState({ simulated: true });
  };
  render() {
    return (
      <div className="about-container center border">
        <div className="team-select">
          <div className="selection">
            <button
              className="button in-selection"
              onClick={this.leftArrow.bind(this, true)}
            >
              Previous
            </button>
            <div className="team-panel">
              <h1>HOME</h1>

              <img src={this.state.homePicture}></img>

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
              className="button in-selection"
              onClick={this.rightArrow.bind(this, true)}
            >
              Next
            </button>
          </div>

          <div className="selection">
            <button
              className="button in-selection"
              onClick={this.leftArrow.bind(this, false)}
            >
              Previous
            </button>
            <div className="team-panel">
              <h1>AWAY</h1>
              <img src={this.state.awayPicture}></img>
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
              className="button in-selection"
              onClick={this.rightArrow.bind(this, false)}
            >
              Next
            </button>
          </div>
        </div>
        <button className="button simulate" onClick={this.simulate}>
          Simulate Matchup
        </button>
        {this.state.simulated ? (
          <SimulationResult
            home={this.state.home}
            homeScore={113}
            homeProbs={"88%"}
            homeLogo={this.state.homePicture}
            away={this.state.away}
            awayScore={108}
            awayProbs={"12%"}
            awayLogo={this.state.awayPicture}
          ></SimulationResult>
        ) : null}
      </div>
    );
  }
}

export default SimulateMatchup;
