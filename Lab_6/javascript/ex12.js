function printer() {
    console.log("Function called");
}
let anon = function() {
    printer();
}
anon();
