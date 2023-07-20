let x = 10;
let y = 7;

function add (x, y, Callback) {
    Callback(x + y);
}

function printer(add) {
    console.log(add);
}


add(x, y, printer);
