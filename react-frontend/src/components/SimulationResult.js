import React from "react";
import "../styles/simulationResult.css";
const SimulationResult = props => {
  return (
    <div className="about">
      <h1>Simulation Result</h1>
      {props.noGame ? (
        <div>
          <br></br>
          <h2>{props.message}</h2>
          <br></br>
        </div>
      ) : (
        <div>
          <div className="result-container">
            <div className="team">
              <img
                src={props.homeLogo}
                className="nba-logo"
                alt="home team logo"
              ></img>
              <div className="result">
                <h2>{props.home + " " + props.homeSeason}</h2>
                <h3>Predicted Score: </h3>
                <h4>{props.homeScore}</h4>
                <h3>Predicted Win Probablity: </h3>
                <h4>{props.homeProbs}</h4>
              </div>
            </div>
            <div className="team">
              <img
                src={props.awayLogo}
                alt="away team logo"
                className="nba-logo"
              ></img>
              <div className="result">
                <h2>{props.away + " " + props.awaySeason}</h2>
                <h3>Predicted Score: </h3>
                <h4>{props.awayScore}</h4>
                <h3>Predicted Win Probablity: </h3>
                <h4>{props.awayProbs}</h4>
              </div>
            </div>
          </div>
          <h3>Overtime Probablity: {props.overtime} </h3>
        </div>
      )}
    </div>
  );
};

export default SimulationResult;
