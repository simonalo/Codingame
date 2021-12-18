function is_happy_nb(n) {
    let reached = [];
    while (Math.abs(n - 1) > 0.001) {
        if (reached.includes(n))
        {
            return false;
        }

        reached.push(n);

        sNumber = n.toString();
        n = 0;
        output = []
        for (var i = 0, len = sNumber.length; i < len; i += 1) {
            n += Math.pow(+sNumber.charAt(i), 2);
        }

    }

    return true;
}

const N = parseInt(readline());
for (let i = 0; i < N; i++) {
    const x = readline();
    if (is_happy_nb(x)) {
        console.log(x + " :)");
    }
    else {
        console.log(x + " :(");
    }
}