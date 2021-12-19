player1_cards = [];
player2_cards = [];
order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];

const n = parseInt(readline()); // the number of cards for player 1
for (let i = 0; i < n; i++) {
    const cardp1 = readline(); // the n cards of player 1
    player1_cards.push(cardp1.substring(0, cardp1.length - 1));
}
const m = parseInt(readline()); // the number of cards for player 2
for (let i = 0; i < m; i++) {
    const cardp2 = readline(); // the m cards of player 2
    player2_cards.push(cardp2.substring(0, cardp2.length - 1));
}
console.error(player1_cards);
console.error(player2_cards);
nb_manches = 0;
pat = false;
bataille = false;
pile1 = [];
pile2 = [];
console.error("DEBUT");
while (player1_cards.length > 0 && player2_cards.length > 0) {
    cardp1 = player1_cards.shift();
    cardp2 = player2_cards.shift();

    index1 = order.indexOf(cardp1);
    index2 = order.indexOf(cardp2);
    if (pile1.length >0)
    {
    console.error("Manche " + nb_manches);
        console.error(player1_cards + " // " + player2_cards);
    console.error(pile1 + " // " + pile2);
    console.error(cardp1 + " // " + cardp2);}

    if (index1 > index2) {
        bataille = false;
        for (let i = 0; i < pile1.length; i++)
        {
            player1_cards.push(pile1[i]);
        }
        player1_cards.push(cardp1);

        for (let i = 0; i < pile1.length; i++)
        {
            player1_cards.push(pile2[i]);
        }
        player1_cards.push(cardp2);

        pile1 = [];
        pile2 = [];
    }
    else if (index1 < index2) {
        bataille = false;
        for (let i = 0; i < pile1.length; i++)
        {
            player2_cards.push(pile1[i]);
        }
        player2_cards.push(cardp1);

        for (let i = 0; i < pile1.length; i++)
        {
            player2_cards.push(pile2[i]);
        }
        player2_cards.push(cardp2);

        pile1 = [];
        pile2 = [];
    }
    else{
        bataille = true;
        if (player1_cards.length < 3 || player2_cards.length < 3) {
            pat = true;
            break;
        }
        else {
            pile1.push(cardp1);
            pile2.push(cardp2);

            for (let i = 0; i < 3; i++)
            {
                cardp1 = player1_cards.shift();
                cardp2 = player2_cards.shift();
                pile1.push(cardp1);
                pile2.push(cardp2);
            }
        }
    }

    if (!bataille) {
        nb_manches++;
    }
}
console.error("FIN");

if (pat) {
    console.error(player1_cards);
    console.error(player2_cards);
    console.error(nb_manches);
    console.log('PAT');
}
else if (player1_cards.length == 0) {
    console.log("2 " + nb_manches);
}
else {
    console.log("1 " + nb_manches);
}
