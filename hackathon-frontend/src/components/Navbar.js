import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Bosh sahifa</Link></li>
        <li><Link to="/teams">Jamoalar</Link></li>
        <li><Link to="/projects">Loyihalar</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;