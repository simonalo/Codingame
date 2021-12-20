const R = parseInt(readline());
const L = parseInt(readline());

var ligne = [R];

for (let etape = 1; etape < L; etape++) {
    var count = 1;
    var new_ligne = [];

    for (let i = 1; i < ligne.length; i++)
    {
        if (ligne[i - 1] != ligne[i]) {
        new_ligne.push(count);
        new_ligne.push(ligne[i - 1]);
        count = 1;
        }
        else {
            count += 1
        }
    }
    new_ligne.push(count);
    new_ligne.push(ligne[ligne.length - 1]);
    ligne = [...new_ligne];
}
var output = "";
ligne.forEach(element => {
    output += element + " "
});
console.log(output.substring(0, output.length - 1));
