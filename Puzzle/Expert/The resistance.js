var morse_symboles = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
];

var M = 20;

function morse(str) {
    var traduction = "";

    for (let i = 0; i < str.length; i++) {
        traduction += morse_symboles[str.charCodeAt(i) - "A".charCodeAt(0)];
    }

    return traduction;
}

function traduire(start, str, dp) {
    if (start == str.length) {
        return 1;
    }

    if (dp[start] != undefined){
        return dp[start];
    }

    var res = 0;
    for (let i = 1; i <= 4 * M && start + i <= str.length; i++) {
        var n = words[str.substr(start, i)];
        if (n !== undefined)
        {
            res += n * traduire(start + i, str, dp);
        }
    }
    return dp[start] = res;
}

var L = readline();
var N = parseInt(readline());

var words = {};
for (let i = 0; i < N; i++) {
    var W = morse(readline());

    if (words[W]){
        words[W]++;
    }
    else{
        words[W] = 1;
    }
}

console.log(traduire(0, L, {}));