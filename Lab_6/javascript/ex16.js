let person = {
    "Name": "John", 
    "Age": "18", 
    "Address": "123 street", 
    "sayHello": function() {
        console.log("Hello my name is " + this.Name)
    }
}

person.sayHello();
