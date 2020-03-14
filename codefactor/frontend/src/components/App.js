import React, { Component } from "react";

import Navbar from "./Navbar";
import Page from "./Page";
// import Blog from "./Blog";



class App extends Component {

    render() {
        return (
            <div className="site">
                <Navbar />
                <Page />
            </div>
        );
    }
}

export default App;