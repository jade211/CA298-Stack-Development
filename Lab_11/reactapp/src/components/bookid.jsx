import { useState, useEffect } from "react";


function Bookid({bookid}){
    const bookid_num = parseInt(bookid);
    const [book, setBook] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);


    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/book/${bookid_num}/`)
        .then(response => response.json())
        .then(data => {
            setBook([data]);
            setIsLoaded(true);
        })
        .catch(error => console.log(error));
    });

    
    const displayFacts = () => {
        return book.map(elem=>
            <div>
            <h2>Book Information on Bookid supplied: {bookid_num}</h2>
                <ul>
                <li><strong>Title: </strong>{elem.title}</li>
                <li><strong>Author: </strong>{elem.author}</li>
                <li><strong>Year: </strong>{elem.year}</li>
                <li><strong>Genre: </strong>{elem.genre}</li>
                <li><strong>Inventory Number: </strong>{elem.inventory_number}</li>
                </ul>
            </div>
        )
    };

    if(isLoaded){
        return (
            <ul>
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

export default Bookid;
