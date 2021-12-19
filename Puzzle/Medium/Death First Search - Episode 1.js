Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};

class Node{
    constructor(id) {
        this.id = id
        this.neighbours = []
        this.neighbours_gate = []
        this.is_gateway = false
    }

    add_neighbour(other) {
        this.neighbours.push(other);
    }

    add_neighbour_gate(other) {
        this.neighbours_gate.push(other);
    }

    remove_neighbour(other) {
        if (other.is_gateway) {
            this.neighbours_gate.remove(other);
            }
        this.neighbours.remove(other);
    }

    set_gateway() {
        this.is_gateway = true
        for (let i = 0; i < this.neighbours.length; i++) {
            var neighbour = this.neighbours[i];
            neighbour.add_neighbour_gate(this);
        }
    }
}

function minimize(graphe, curr_node) {
    graphe_min = [];
    for (let i = 0; i < graphe.length; i++) {
        const node_tmp = graphe[i];
        graphe_min.push(new Node(node_tmp.id));
    }
    for (let i = 0; i < graphe.length; i++) {
        node_tmp = graphe[i];
        node_min = graphe_min[i];
        node_min.is_gateway = node_tmp.is_gateway;

        for (let j = 0; j < node_tmp.neighbours_gate.length; j++)
        {
            neighbour_gate_tmp = node_tmp.neighbours_gate[j];
            node_min.neighbours_gate.push(graphe_min[neighbour_gate_tmp.id]);
        }

        for (let k = 0; k < node_tmp.neighbours_gate.length; k++)
        {
            neighbour_tmp = node_tmp.neighbours_gate[k];

            if (node_tmp == curr_node || node_min.neighbours_gate.length > 0) {
                node_min.neighbours.push(graphe_min[neighbour_tmp.id]);
            } else if (neighbour_tmp.id == curr_node.id) {
                node_min.neighbours.push(graphe_min[neighbour_tmp.id]);
            }
        }
    }
    return graphe_min;
}

function find_min_dist(Q, dist) {
    min_dist = -1;

    for (let i = 0; i < Q.length; i++) {
        node_tmp = Q[i];

        if (min_dist == -1 || min_dist > dist.get(node_tmp)) {
            min_dist = dist.get(node_tmp);
            min_node = node_tmp;
        }
    }

    return [min_node, min_dist];
}

function dijkstra(graphe, node_start) {
    Q = [];
    dist = new Map();
    prev = new Map();

    for (let i = 0; i < graphe.length; i++) {
        node_tmp = graphe[i];
        dist.set(node_tmp, Math.inf);
        prev.set(node_tmp, null);
        Q.push(node_tmp);
    }
    dist.set(node_start, 0);

    while (Q.length > 0) {
        values = find_min_dist(Q, dist);
        var u = values[0];
        var min_dist = values[1];
        if (min_dist == Math.inf) {
            return [dist, prev];
        }

        Q.remove(u);

        for (let i = 0; i < u.neighbours.length; i++) {
            v = u.neighbours[i];
            alt = dist.get(u) + 1;
            if (alt < dist.get(v)) {
                dist.set(v, alt);
                prev.set(v, u);
            }
        }
    }
    return [dist, prev];
}

function find_node_to_cut(dist, prev, curr_node, graphe) {
    if (curr_node.neighbours_gate.length > 0) {
        return [curr_node, curr_node.neighbours_gate[0]];
    }
    graphe_minimize = minimize(graphe, curr_node);
    node_start_min = graphe_minimize[curr_node.id];
    var values = dijkstra(graphe_minimize, node_start_min);
    var dist_min = values[0];
    var prev_min = values[1];

    node_priority = null;
    gate_priority = null;
    priority = -10;

    for (const [node_tmp, dist_tmp] of dist_min.entries()) {
        if (dist_tmp != Math.inf && node_tmp.neighbours_gate.length >= 2) {
            if (priority == -10 || priority > dist_tmp - len(node_tmp.neighbours_gate)) {
                priority = dist_tmp - len(node_tmp.neighbours_gate);
                node_priority = node_tmp;
                gate_priority = node_tmp.neighbours_gate[0];
            }
        }
    }
    if (priority == -10) {
        for (const [node_tmp, dist_tmp] of dist_min.entries()) {
            if (node_tmp.neighbours_gate.length >= 2) {
                priority = 0;
                node_priority = node_tmp;
                gate_priority = node_tmp.neighbours_gate[0];
            }
        }
    }

    if (priority == -10) {
        for (const [node_tmp, dist_tmp] of dist_min.entries()) {
            if (node_tmp.neighbours_gate.length >= 1) {
                node_priority = node_tmp;
                gate_priority = node_tmp.neighbours_gate[0];
            }
        }
    }

    node_priority = graphe[node_priority.id];
    gate_priority = graphe[gate_priority.id];
    return [node_priority, gate_priority];
}

var inputs = readline().split(' ');
const N = parseInt(inputs[0]); // the total number of nodes in the level, including the gateways
const L = parseInt(inputs[1]); // the number of links
const E = parseInt(inputs[2]); // the number of exit gateways

graphe = [];
for (let i = 0; i < N; i++) {
    graphe.push(new Node(i));
}
gateways = [];

for (let i = 0; i < L; i++) {
    var inputs = readline().split(' ');
    const N1 = parseInt(inputs[0]); // N1 and N2 defines a link between these nodes
    const N2 = parseInt(inputs[1]);

    node1 = graphe[N1];
    node2 = graphe[N2];
    node1.add_neighbour(node2);
    node2.add_neighbour(node1);
}

for (let i = 0; i < E; i++) {
    const EI = parseInt(readline()); // the index of a gateway node
    graphe[EI].set_gateway();
    gateways.push(graphe[EI]);
}

// game loop
while (true) {
    const SI = parseInt(readline()); // The index of the node on which the Bobnet agent is positioned this turn

    var node_start = graphe[SI];
    var values = dijkstra(graphe, node_start);
    var dist = values[0];
    var prev = values[1];

    var values2 = find_node_to_cut(dist, prev, graphe[SI], graphe);
    var node_to_rem_link = values2[0];
    var nearest_gateway = values2[1];

    console.log(nearest_gateway.id + " " + node_to_rem_link.id);
    nearest_gateway.remove_neighbour(node_to_rem_link);
    node_to_rem_link.remove_neighbour(nearest_gateway);
}
