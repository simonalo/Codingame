const N = parseInt(readline());
var list_x = [];
var list_y = [];
var min_x;
var max_x;
for (let i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    const X = parseInt(inputs[0]);
    const Y = parseInt(inputs[1]);
    if (i == 0)
    {
        min_x = X;
        max_x = X;
    }
    min_x = Math.min(min_x, X);
    max_x = Math.max(max_x, X);
    list_x.push(X);
    list_y.push(Y);
}

function median(values){
  if(values.length ===0) throw new Error("No inputs");

  values.sort(function(a,b){
    return a-b;
  });

  var half = Math.floor(values.length / 2);
  console.error(values[half]);
  if (values.length % 2)
    return values[half];

  return (values[half]);
}

var pos_main;
var copy_y = [...list_y];
var median_y = median(copy_y);
var longueur = max_x - min_x;

for (let i = 0; i < N; i++) {
    longueur += Math.abs(list_y[i] - median_y);
}

console.log(longueur);
