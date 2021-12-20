let budgets = [];
let participations = [];

const N = parseInt(readline());
const C = parseInt(readline());
for (let i = 0; i < N; i++) {
    const B = parseInt(readline());
    budgets.push(B);
    participations.push(0);
}

const sum = budgets.reduce((partial_sum, a) => partial_sum + a, 0);

if (sum < C) {
    console.log('IMPOSSIBLE');
}
else {
    var total_participation = 0;
    oods = 0;
    while (total_participation < C) {
        if (oods == N){
            oods = 0;
        }
        if (participations[oods] < budgets[oods]) {
            participations[oods] += 1;
            total_participation++;
        }

        oods++;
    }
    participations.sort(function(a, b) {
    return a - b;
    });
    participations.forEach(element => {
        console.log(element);
    });
}
