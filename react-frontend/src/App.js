import React from "react";
import Banner from "./components/banner";
import Footer from "./components/footer";
import About from "./components/about";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Banner></Banner>
      <body>
        <About></About>
      </body>

      <Footer></Footer>
    </div>
  );
}

export default App;
