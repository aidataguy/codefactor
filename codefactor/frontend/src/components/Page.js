import React from 'react'
import { Switch, Route } from "react-router-dom";
import Login from "./login";
import Signup from "./signup";

export default function Page() {
    return(
        <main>
            <h1>Ahhh after 10,000 years I'm free. Time to conquer the Earth!</h1>

            <Switch>
                <Route exact path={"/login/"} component={Login} />
                <Route exact path={"/signup/"} component={Signup} />
                <Route path={"/"} render={() => <div>Home again</div>} />
            </Switch>
        </main>
    )
}