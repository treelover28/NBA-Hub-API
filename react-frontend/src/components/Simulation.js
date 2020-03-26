import React from "react";
import SimulationPanel from "./SimulationPanel";
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
    if (this.state.buttonName === "Reset Panel") {
      this.setState({ showOption: false, buttonName: "Predict" });
    } else {
      this.setState({ showOption: true, buttonName: "Reset Panel" });
    }
  };

  getOptionState = () => {
    return this.state.showOption;
  };

  render() {
    return (
      <div className="simulationPanel">
        {/* Clicking button will show 
        the two simulation options */}

        <button className="button" onClick={this.showOption}>
          {this.state.buttonName}
        </button>

        {/* Pass function to child component props so when a simulation type is chosen, 
          we don't show the other option anymore, but instead show the simulation panel running 
          */}
        {this.state.showOption ? (
          <SimulationPanel
            showOption={this.showOption}
            getOptionState={this.getOptionState}
          ></SimulationPanel>
        ) : null}
      </div>
    );
  }
}

export default Simulation;
