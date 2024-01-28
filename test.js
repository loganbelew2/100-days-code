const x = 2;
let y = 4;

function update(arg) {
    return Math.random() + y * arg;
}

if (y === 4) {
    y = 6;
} else {
    y = 7;
}

const result = update(x);
