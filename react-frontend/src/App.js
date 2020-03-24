import React from "react";
import Banner from "./components/Banner";
import Footer from "./components/Footer";
import About from "./components/About";
import Simulation from "./components/Simulation";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Banner></Banner>
      <About></About>
      <Simulation></Simulation>
      <br></br>
      <br></br>
      <Footer></Footer>
    </div>
  );
}

export default App;
