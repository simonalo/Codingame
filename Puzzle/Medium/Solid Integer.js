var n = BigInt(readline());
var maxi = BigInt(parseInt(n, 10));

var digits = [1];
var sum = BigInt(1);
while (sum + BigInt(9 ** (digits.length)) <= BigInt(n)) {
    sum += BigInt(9) ** BigInt((digits.length));

    digits.push(1);
}

nb_eme = BigInt(sum);

function check(digits, pos, maxi, curr) {
    let total = BigInt(1);
    for (let i = pos + 1; i < digits.length; i++) {
        total *= BigInt(9);
    }

    return BigInt(BigInt(curr) + BigInt(total)) <= BigInt(maxi);
}

var pos = 0;
while (BigInt(nb_eme) < BigInt(n) && pos < digits.length)
{
    if (check(digits, pos, BigInt(n), BigInt(nb_eme))) {
        digits[pos] += 1;
        total = BigInt(1);
        for (let i = pos + 1; i < digits.length; i++) {
            total *= BigInt(9);
        }

        nb_eme += BigInt(total);
    }
    else{
        pos += 1;
    }
}

function convertArrayToNumber(arr) {
    let result = ""
    for (el of arr) {
        result += el
    }
    return result
}

var final = 0;
var k = digits.length;
var digits_string = [];
for (let i = 0; i < k; i++) {
    digits_string.push(digits[i].toString(10));

}
console.log(convertArrayToNumber(digits_string));