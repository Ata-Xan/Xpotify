import React, {Component} from "react"
import {render} from "react-dom";
import HomePage from "./Homepage"


// I need to render this component inside the div in index.html
export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div> 
                <HomePage/>
            </div>  
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);