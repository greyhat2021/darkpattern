
import './App.css';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Homepage from './Homepage';
import Detectpage from './Detectpage';
import Resultpage from './Resultpage';
import AboutUs from './AboutUs';
import Reviewresult from './ReviewResult';

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav className='navbar'>
          <Link to="/">HOME</Link>
          <img src="genuine-kart-high-resolution-logo-transparent.png" width={200} className='img-logo'></img>
          <Link to="/about-project">ABOUT PROJECT</Link>

        </nav>
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/detect" element={<Detectpage />} />
          <Route path="/result" element={<Resultpage />} />
          <Route path="/about-project" element={<AboutUs />} />
          <Route path='/reviewresult' element={<Reviewresult/>}/>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
