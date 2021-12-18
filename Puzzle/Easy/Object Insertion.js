/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

grid = [];
object = [];

var inputs = readline().split(' ');
const a = parseInt(inputs[0]);
const b = parseInt(inputs[1]);

for (let i = 0; i < a; i++) {
    const objectLine = readline();
    object.push(objectLine.split(''))
}

var inputs = readline().split(' ');
const c = parseInt(inputs[0]);
const d = parseInt(inputs[1]);

for (let i = 0; i < c; i++) {
    const gridLine = readline();
    grid.push(gridLine.split(''))
}

first = false;
grid_first = [];
nb = 0;
for (let i = 0; i < c - a + 1; i++) {
    for (let j = 0; j < d - b + 1; j++) {
        stop = false;
        for (let k = 0; k < a; k++) {
            if (stop)
            {
                break;
            }

            for (let l = 0; l < b; l++) {
                if (object[k][l] == ".") {
                    continue;
                }
                else {
                    if (grid[i + k][j + l] == "#"){
                        stop = true;
                        break;
                    }
                }

            }
        }
        if (!stop) {
            nb++;
            if (!first){
                first = true;
                for (let m = 0; m < grid.length; m++) {
                    grid_first[m] = grid[m].slice();
                }
                for (let k = 0; k < a; k++) {
                    for (let l = 0; l < b; l++) {
                        if (object[k][l] == "*") {
                            grid_first[i + k][j + l] = "*";
                        }
                    }
                }
            }
        }
    }
}


console.log(nb);
if (nb == 1) {
    for (let i = 0; i < grid_first.length; i++) {
        console.log(grid_first[i].join(''));
    }
}