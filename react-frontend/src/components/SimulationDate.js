import React from "react";
import img_calendar from "../images/calendar.jpg";
import "../styles/simulationDate.css";
class SimulationDate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: ""
    };
  }

  getDateResult = date => {};

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
                <label htmlFor="date-simulation">
                  Enter a future game date you wish to simulate
                </label>
                <form
                  action=""
                  id="date-simulation"
                  method="post"
                  target="about"
                >
                  <input
                    type="date"
                    className="date-input"
                    //   max="2020-04-15"
                    required
                  />
                  <br />
                  <button type="submit" className="button">
                    Submit Date
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default SimulationDate;
