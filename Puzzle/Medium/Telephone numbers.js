class Node {
    constructor(nb){
        this.nb = nb;
        this.childs = [];
    }

    addChild(new_num) {
        if (new_num.length == 0) {
            return;
        }

        var first_digit = parseInt(new_num.charAt(0))
        var found = false;
        this.childs.forEach(child => {
            if (child.nb == first_digit) {
                child.addChild(new_num.substring(1));
                found = true;
                return;
            }
        });
        if (found){
            return;
        }
        // If we reach this code, no child have first_digit as nb
        var new_child = new Node(first_digit);
        this.childs.push(new_child);
        new_child.addChild(new_num.substring(1));
    }

    countNbDigits() {
        if (this.childs.length == 0) {
            return 1;
        }

        var total = 0;
        this.childs.forEach(child => {
            total += child.countNbDigits();
        });

        return total + 1;
    }
}

function find_root(node_list, digit) {
    var good_node = false;
    node_list.forEach(node => {
        if (node.nb == digit) {
            good_node = node;
        }
    });

    if (good_node != false) {
        return good_node
    }

    new_root = new Node(digit);
    node_list.push(new_root)
    return new_root;
}

var roots = [];
const N = parseInt(readline());
for (let i = 0; i < N; i++) {
    const telephone = readline();
    let digit = parseInt(telephone[0]);
    var root = find_root(roots, digit);
    root.addChild(telephone.substring(1));
}

var total = 0;
roots.forEach(root => {
    total += root.countNbDigits();
});

console.log(total);
