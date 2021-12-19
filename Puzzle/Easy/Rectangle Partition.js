var inputs = readline().split(' ');
const w = parseInt(inputs[0]);
const h = parseInt(inputs[1]);
const countX = parseInt(inputs[2]);
const countY = parseInt(inputs[3]);
var inputs = readline().split(' ');
var list_x = [0];
var list_y = [0];

for (let i = 0; i < countX; i++) {
    const x = parseInt(inputs[i]);
    list_x.push(x);
}
list_x.push(w);
var inputs = readline().split(' ');
for (let i = 0; i < countY; i++) {
    const y = parseInt(inputs[i]);
    list_y.push(y);
}
list_y.push(h)
var nb_square = 0;
for (let k = 0; k < list_y.length; k++) {
    var last_y = list_y[k];
    for (let i = k + 1; i < list_y.length; i++) {
        const y = list_y[i];
        for (let l = 0; l < list_x.length; l++) {
            var last_x = list_x[l];
            for (let j = l + 1; j < list_x.length; j++) {
                const x = list_x[j];
                if (x - last_x == y - last_y) {
                    nb_square++;
                }
            }
        }
    }
}

console.log(nb_square);
