
import React from "react";
import './Homepage.css';
import { Link } from "react-router-dom";

function Homepage() {
  return (
    <div>
      <div className="home-container">
        <div className="heading">
          <h1 className="highlightgreen">TRAP TRACKERS</h1>
          <h4>SUDHARSANA I (TEAM LEAD)</h4>
          <h4>VISHNU DEEPAN P</h4>
          <h4>TEJASH DHAKSHIN S</h4>
          <h4>BALA CHIBI HARIESH B</h4>

        </div>
        {/* <div className="policy-div">
          <p>
            Dark patterns are deceptive design practices in user interfaces or user experiences across platforms.
            These practices aim to mislead or trick users into taking actions they did not originally intend or want to perform.
            These are called wrongful or unethical practices
          </p>
        </div> */}
        <div className="detect-container">
          <Link to="/detect" className="detect-link">DETECT</Link>
        </div>
      </div>
    </div>
  )
}

export default Homepage;
