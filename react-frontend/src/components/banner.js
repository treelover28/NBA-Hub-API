import React from "react";
import logo from "../images/bball-logo.svg";
import "../styles/banner.css";
const Banner = () => {
  return (
    <div className="banner">
      <img
        src={logo}
        className="logo"
        alt="website logo. A black basketball."
      ></img>
      <div className="banner-title-container">
        <h1 className="banner-title">NBA Hub</h1>
      </div>
    </div>
  );
};

export default Banner;
