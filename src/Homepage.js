
import React from "react";
import './Homepage.css';
import { Link } from "react-router-dom";

function Homepage() {
  return (
    <div>
      <div className="home-container">
        <div className="heading">
          <h1>FLIPKART DARK PATTERN DETECTOR</h1>
          <h3>WHAT IS A DARK PATTERN ?</h3>
        </div>
        <div className="policy-div">
          <p>
            Dark patterns are deceptive design practices in user interfaces or user experiences across platforms.
            These practices aim to mislead or trick users into taking actions they did not originally intend or want to perform.
            These are called wrongful or unethical practices
          </p>
        </div>
        <div className="detect-container">
          <Link to="/detect" className="detect-link">DETECT</Link>
        </div>
      </div>
    </div>
  )
}

export default Homepage;
