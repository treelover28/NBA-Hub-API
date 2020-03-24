import React from "react";
// import logo from "../images/bball-logo.svg";
import logo from "../images/logo.gif";
import "../styles/banner.css";
const Banner = () => {
  return (
    <div className="banner">
      <img
        src={logo}
        className="site-logo"
        alt="website logo. An orange basketball."
      ></img>
      <div className="banner-title-container">
        <h1 className="banner-title">NBA HUB</h1>
      </div>
    </div>
  );
};

export default Banner;
