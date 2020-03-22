import React from "react";
import Banner from "./components/banner";
import Footer from "./components/footer";
import About from "./components/about";
import Simulation from "./components/simulation";
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
