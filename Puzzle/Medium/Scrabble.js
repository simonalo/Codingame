// Construction du dictionnaire
var dict = {};
dict["e"] = 1;
dict["a"] = 1;
dict["i"] = 1;
dict["o"] = 1;
dict["n"] = 1;
dict["r"] = 1;
dict["t"] = 1;
dict["l"] = 1;
dict["s"] = 1;
dict["u"] = 1;
dict["d"] = 2;
dict["g"] = 2;
dict["b"] = 3;
dict["c"] = 3;
dict["m"] = 3;
dict["p"] = 3;
dict["f"] = 4;
dict["h"] = 4;
dict["v"] = 4;
dict["w"] = 4;
dict["y"] = 4;
dict["k"] = 5;
dict["j"] = 8;
dict["x"] = 8;
dict["q"] = 10;
dict["z"] = 10;

// Construction de la liste de mots autorisés
var mots_autor = [];
const N = parseInt(readline());
for (let i = 0; i < N; i++) {
    const W = readline();
    mots_autor.push(W);
}

// Construction de la liste des lettres disponibles
const LETTERS = readline();
var letters_array = [];
for (let i = 0; i < LETTERS.length; i++) {
    const lettre = LETTERS[i];
    letters_array.push(lettre);
}

// On regarde quel mot peut faire le plus de points et est constructible
var max_points = 0;
var mot_max = "";
mots_autor.forEach(mot => {
    // On regarde chaque mot du dico
    let mot_point = 0;
    let possible = true;
    let copy_letters = [...letters_array];
    // Pour chaque lettre du mot : on vérifie si elle est disponible
    for (let i = 0; i < mot.length; i++) {
        const lettre_mot = mot[i];
        const index = copy_letters.indexOf(lettre_mot);
        if (index > -1) {
            // Lettre dispo : on la retire de copy_letters (on l'utilise)
            mot_point += dict[lettre_mot]
            copy_letters.splice(index, 1);
        }
        else {
            // Lettre pas dispo : on arrête et on réinitialise mot_points
            possible = false;
            mot_point = 0;
            break
        }
    }
    // On vérifie si le mot contructible vaut plus de points que le précédent constructible
    if (mot_point > max_points) {
        mot_max = mot;
        max_points = mot_point;
    }
});

console.log(mot_max);
