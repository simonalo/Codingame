const n = parseInt(readline());

res = 0
quotient = n
p = 2
while (p <= quotient) {
    while (quotient % p == 0) {
        quotient = Math.floor(quotient/p)
        res += n / p
    }
    p += 1
}

console.log(res)
