import React from "react";
import "../styles/simulation.css";
import img_calendar from "../images/calendar.jpg";
import img_matchup from "../images/matchup.jpg";
class SimulationPanel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      simulateDate: false,
      simulateMatchup: false
    };
  }

  render() {
    return (
      <div className="simulationPanel">
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
                  Pellentesque habitant morbi tristique senectus et netus et
                  malesuada fames ac turpis egestas. Vestibulum tortor quam,
                  feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu
                  libero sit amet quam egestas semper.
                </p>
                <button className="button">SIMULATE BY DATE</button>
              </div>
            </div>
          </div>
        </div>

        <div className="about-container decrease-top">
          <div className="about">
            <h1>SIMULATION BY DATE</h1>
            <div className="info">
              <img
                src={img_matchup}
                className="img-in-box"
                alt="Giannis playing against Kawhi Leonard."
              ></img>
              <div className="text-button">
                <p>
                  Pellentesque habitant morbi tristique senectus et netus et
                  malesuada fames ac turpis egestas. Vestibulum tortor quam,
                  feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu
                  libero sit amet quam egestas semper.
                </p>
                <button className="button">SIMULATE BY DATE</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default SimulationPanel;
