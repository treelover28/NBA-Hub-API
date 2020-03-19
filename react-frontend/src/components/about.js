import React from "react";
import "../styles/about.css";
import players from "../images/players.jpg";
const About = () => {
  return (
    <div className="about-container">
      <h1 className="section-header">About this page</h1>
      <div className="picture-container">
        <img
          src={players}
          className="picture"
          alt="background showing three NBA players"
        ></img>
      </div>
      <button className="button">PREDICT</button>
      <div className="about">
        <p className="intro">
          Pellentesque habitant morbi tristique senectus et netus et malesuada
          fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae,
          ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam
          egestas semper. Pellentesque habitant morbi tristique senectus et
          netus et malesuada fames ac turpis egestas. Vestibulum tortor quam,
          feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero
          sit amet quam egestas semper.
        </p>
      </div>
    </div>
  );
};

export default About;
