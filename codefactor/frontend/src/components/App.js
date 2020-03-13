import React, { Component } from "react";
import { Switch, Route } from "react-router-dom";
import Login from "./login";
import Signup from "./signup";
import Navbar from "./Navbar";


class App extends Component {

    render() {
        return (
            <div className="site">
                <Navbar />
                <main>
                    <h1>Ahhh after 10,000 years I'm free. Time to conquer the Earth!</h1>

                    <Switch>
                        <Route exact path={"/login/"} component={Login} />
                        <Route exact path={"/signup/"} component={Signup} />
                        <Route path={"/"} render={() => <div>Home again</div>} />
                    </Switch>
                </main>
            </div>
        );
    }
}

export default App;