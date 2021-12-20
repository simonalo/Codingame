class Node {
    constructor(nb) {
        this.nb = nb;
        this.childs = [];
        this.parents = [];
    }

    addChild(new_child) {
        this.childs.push(new_child);
    }

    addParent(new_parent) {
        this.parents.push(new_parent);
    }

    findLongestPath() {
        var length = 0;

        if (this.childs.length == 0) {
            return 1;
        }

        this.childs.forEach(child => {
            let length_temp = child.findLongestPath();
            if (length_temp > length) {
                length = length_temp;
            }

        });

        return 1 + length;
    }
}

var dict = {};

const n = parseInt(readline()); // the number of relationships of influence
for (let i = 0; i < n; i++) {
    var inputs = readline().split(' ');
    const x = parseInt(inputs[0]); // a relationship of influence between two people (x influences y)
    const y = parseInt(inputs[1]);

    var node_1, node_2;
    if (x.toString() in dict){
        node_1 = dict[x.toString()];
    }
    else {
        node_1 = new Node(x);
        dict[x.toString()] = node_1;
    }

    if (y.toString() in dict){
        node_2 = dict[y.toString()];
    }
    else {
        node_2 = new Node(y);
        dict[y.toString()] = node_2;
    }

    node_1.addChild(node_2);
    node_2.addParent(node_1);
}

length = 0;

for(var key in dict) {
    var node = dict[key];
    if (node.parents.length == 0) {
        var length_tmp = node.findLongestPath();
        length = Math.max(length_tmp, length);
    }
}

console.log(length);
