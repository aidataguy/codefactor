import React, { useState } from 'react'
import axiosInstance from "../axiosApi";
import { Link } from "react-router-dom";
import Logout from './login'

export default function Navbar() {
    const [loggedIn, setLoggedIn] = useState(false);
    const handleLogout = async () => {
        try {
            const response = await axiosInstance.post('/blacklist/', {
                "refresh_token": localStorage.getItem("refresh_token")
            });
            console.log(" response is.....", response)
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            axiosInstance.defaults.headers['Authorization'] = null;
            return response;
        }
        catch (e) {
            console.log(e);
        }
    };

    return (
            <nav>
                <Link className={"nav-link"} to={"/"}>Home</Link>
                { loggedIn ?
                    <Link onClick={handleLogout} to={"/logout"}>Logout</Link>
                    :
                    <p>You are LoggedIN!!</p>
                }
                {/* <React.Fragment> */}
                        <Link className={"nav-link"} to={"/login/"} >Login</Link>
                        <Link className={"nav-link"} to={"/signup/"}>Signup</Link>
                {/* </React.Fragment> */}

            </nav>
    )
}
