import { useState, useEffect } from "react";


function BookList(){
    const [book, setBook] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);


    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/book/`)
        .then(response => response.json())
        .then(data => {
            setBook(data.map(element => element));
            setIsLoaded(true);
        })
        .catch(error => console.log(error));
    });

    
    const displayFacts = () => {
        return book.map(elem=>
            <div>
                <ul>
                <li><strong>Title: </strong>{elem.title}</li>
                <li><strong>Author: </strong>{elem.author}</li>
                <li><strong>Year: </strong>{elem.year}</li>
                <li><strong>Genre: </strong>{elem.genre}</li>
                <li><strong>Inventory Number: </strong>{elem.inventory_number}</li>
                </ul>
                <br></br>
            </div>
        )
    };

    if(isLoaded){
        return (
            <ul>
                <h2>Book Information</h2>
                {displayFacts()}
            </ul>
        )
    }
    else{
        return (
            <p>Loading Book Information...</p>
        )
    }
}

export default BookList;
