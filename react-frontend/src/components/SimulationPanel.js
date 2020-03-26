import React from "react";
import "../styles/simulation.css";
import img_calendar from "../images/calendar.jpg";
import img_matchup from "../images/matchup.jpg";
import SimulationDate from "./SimulationDate";
import SimulationMatchup from "./SimulateMatchup";
class SimulationPanel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      simulateDate: false,
      simulateMatchup: false,
      showMenu: true
    };
  }

  simulateByDate = () => {
    // mutually exclusive events
    // this.props.showOption();
    this.setState({
      simulateDate: true,
      simulateMatchup: false,
      showMenu: false
    });
    // close option menu
  };

  simulateByMatchup = () => {
    this.setState({
      simulateMatchup: true,
      simulateDate: false,
      showMenu: false
    });
    // this.props.showOption();
    // close option menu
    // alert("Simulate By Matchup");
  };
  render() {
    return (
      <div className="simulationPanel">
        {this.state.showMenu ? (
          <div className="simulation-menu">
            <div className="about-container decrease-top">
              <div className="about">
                <h1>SIMULATION BY DATE</h1>
                <div className="info">
                  <img
                    src={img_calendar}
                    className="img-in-box"
                    alt="Lebron in front of a calendar."
                  ></img>
                  <div className="text-button">
                    <p>
                      Choose a date to generate predictions for games on that
                      date!
                    </p>
                    <p>
                      You can also select dates from the past, from 2014-09-01
                      up to now, to see what the algorithm think should have
                      happened and compare real-life results!
                    </p>
                    <button className="button" onClick={this.simulateByDate}>
                      SIMULATE BY DATE
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div className="about-container decrease-top">
              <div className="about">
                <h1>SIMULATION BY MATCHUP</h1>
                <div className="info">
                  <img
                    src={img_matchup}
                    className="img-in-box"
                    alt="Giannis playing against Kawhi Leonard."
                  ></img>
                  <div className="text-button">
                    <p>
                      Choose two teams and their corresponding season to
                      matchup!
                    </p>
                    <p>
                      For example, you can simulate what would happen if the
                      2017 Warriors plays the 2020 Lakers!
                    </p>
                    <p>Give it a try!</p>
                    <button className="button" onClick={this.simulateByMatchup}>
                      SIMULATE BY MATCHUP
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ) : null}

        {/* conditionally render the simulation pages */}
        {this.state.simulateDate ? <SimulationDate></SimulationDate> : null}
        {this.state.simulateMatchup ? (
          <SimulationMatchup></SimulationMatchup>
        ) : null}
      </div>
    );
  }
}

export default SimulationPanel;
