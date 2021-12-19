const n = parseInt(readline());

var dict = {};
var maxLen = 0;
for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    const b = inputs[0];
    const c = parseInt(inputs[1]);
    dict[b] = String.fromCharCode(c);

    if (b.length > maxLen) {
        maxLen = b.length;
    }
}
const s = readline();

var currString = "";
var res = "";
var currLen = 0;
var index = 0;
var reachedEnd = true;
var last_index = 0;

while (index < s.length) {
    currLen++;
    currString += s[index];
    if (currLen > maxLen) {
        reachedEnd = false;
        break;
    }
    else if (currString in dict){
        res += dict[currString];
        currLen = 0;
        currString = "";
        last_index = index + 1;
    }
    index++;
}

if (reachedEnd && currLen == 0) {
    console.log(res);
} else {
    console.log("DECODE FAIL AT INDEX", last_index);
}
