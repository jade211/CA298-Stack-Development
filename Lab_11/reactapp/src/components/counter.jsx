import { useState } from "react";

function Counter(){
    const [myVar, setMyVar] = useState(0);
	// const [stringVar, setStringVar] = useState("Hi"); // string
	// const [objVar, setObjVar] = useState({'type':'initial'}) // json object
	// const [arrVar, setArrVar] = useState([1,2,3]); // array

    return (
        <div>
        <h3>Clicks: {myVar}</h3>
        <button onClick={
            ()=>{
                setMyVar(myVar + 1)
            }
        }>Click me </button>
        </div>
    )
}

export default Counter;
