import React, { Component } from "react";
// import axiosFileInstance from "../axiosApi";
import axios from 'axios'
class Signup extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: "",
            email: "",
            slug_name: "",
            avatar: "",

            errors: {}
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleImageChange = this.handleImageChange.bind(this);

    }

    handleChange(event) {
        this.setState({ [event.target.name]: event.target.value });

        if (event.target.name === 'username')
            this.setState({ slug_name: event.target.value })
    }

    handleImageChange(event) {
        console.log(event.target.files[0])
        this.setState({
            avatar: event.target.files[0]
        })
    };

    async handleSubmit(event) {
        event.preventDefault();
        console.log(this.state)
        try {
            const formData = new FormData();

            formData.append("username", this.state.username);
            formData.append("email", this.state.email);
            formData.append("password", this.state.password);
            formData.append("slug_name", this.state.slug_name);
            formData.append("avatar", this.state.avatar, this.state.avatar.name);

            const response = await axios.post('http://localhost:8000/api/v1/user/create/', formData, {
                headers: { 'content-type': 'multipart/form-data' }
            });
            return response;
        } catch (error) {
            console.log(error);
            this.setState({
                errors: error.response.data
            });
        }
    }


    render() {
        return (
            <div>
                Signup
                <form onSubmit={this.handleSubmit}>
                    <div>
                        <label className="label">Username:</label>
                        <input name="username" type="text" value={this.state.username} onChange={this.handleChange} />
                        {this.state.errors.username ? this.state.errors.username : null}
                    </div>
                    <div>
                        <label className="avatar">avatar:</label>
                        <input name="avatar" type="file" accept="image/png, image/jpeg" onChange={this.handleImageChange} />

                    </div>
                    <label>
                        Email:
                        <input name="email" type="email" value={this.state.email} onChange={this.handleChange} />
                        {this.state.errors.email ? this.state.errors.email : null}
                    </label>
                    <label>
                        Password:
                        <input name="password" type="password" value={this.state.password} onChange={this.handleChange} />
                        {this.state.errors.password ? this.state.errors.password : null}
                    </label>
                    <label>
                        Slug:
                        <input name="slug_name" type="hidden" value={this.state.slug_name} onChange={this.handleChange} />
                        {this.state.errors.slug_name ? this.state.errors.slug_name : null}

                    </label>

                    <input type="submit" value="Submit" />
                </form>
            </div>
        )
    }
}

export default Signup;