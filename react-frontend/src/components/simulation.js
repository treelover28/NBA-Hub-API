import React from "react";
import SimulationPanel from "./simulationPanel";
import "../styles/simulation.css";
class Simulation extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showOption: false,
      buttonName: "Predict"
    };
  }

  showOption = () => {
    if (this.state.buttonName === "Close Panel") {
      this.setState({ showOption: false, buttonName: "Predict" });
    } else {
      this.setState({ showOption: true, buttonName: "Close Panel" });
    }
  };

  render() {
    // implement class
    return (
      <div className="simulationPanel">
        <button className="button" onClick={this.showOption}>
          {this.state.buttonName}
        </button>
        {this.state.showOption ? <SimulationPanel></SimulationPanel> : null}
      </div>
    );
  }
}

export default Simulation;
