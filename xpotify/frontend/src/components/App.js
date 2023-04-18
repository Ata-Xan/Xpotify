import React, {Component} from "react"
import {render} from "react-dom";


// I need to render this component inside the div in index.html
export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return <h1>Testing React Code</h1>;
    }
}

const appDiv = document.getElementById("app")
render(<App/>, appDiv);