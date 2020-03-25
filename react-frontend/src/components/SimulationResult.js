import React from "react";
import "../styles/simulationResult.css";
const SimulationResult = props => {
  return (
    <div className="about">
      <h1>Simulation Result</h1>
      <div className="result-container">
        <div className="home">
          <img
            src={props.homeLogo}
            className="nba-logo"
            alt="home team logo"
          ></img>
          <div className="result">
            <h2>{props.home + " " + props.homeSeason}</h2>
            <h4>Predicted Score: </h4>
            <h5>{props.homeScore}</h5>
            <h4>Predicted Win Probablity: </h4>
            <h5>{props.homeProbs}</h5>
          </div>
        </div>
        <div className="away">
          <img
            src={props.awayLogo}
            alt="away team logo"
            className="nba-logo"
          ></img>
          <div className="result">
            <h2>{props.away + " " + props.awaySeason}</h2>
            <h4>Predicted Score: </h4>
            <h5>{props.awayScore}</h5>
            <h4>Predicted Win Probablity: </h4>
            <h5>{props.awayProbs}</h5>
          </div>
        </div>
      </div>
      <h4>Overtime Probablity: {props.overtime} </h4>
    </div>
  );
};

export default SimulationResult;
