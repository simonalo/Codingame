import math


class Node:
    def __init__(self, id_node):
        self.id = id_node
        self.neighbours = []
        self.neighbours_gate = []
        self.is_gateway = False

    def add_neighbour(self, other):
        self.neighbours.append(other)

    def add_neighbour_gate(self, other):
        self.neighbours_gate.append(other)

    def remove_neighbour(self, other):
        if other.is_gateway:
            self.neighbours_gate.remove(other)
        self.neighbours.remove(other)

    def set_gateway(self):
        self.is_gateway = True
        for neighbour in self.neighbours:
            neighbour.add_neighbour_gate(self)

    def __hash__(self):
        return self.id


def minimize(graphe, curr_node):
    graphe_min = [Node(node_tmp.id) for node_tmp in graphe]

    for i, node_tmp in enumerate(graphe):
        node_min = graphe_min[i]
        node_min.is_gateway = node_tmp.is_gateway

        for neighbour_gate_tmp in node_tmp.neighbours_gate:
            node_min.neighbours_gate.append(graphe_min[neighbour_gate_tmp.id])

        for neighbour_tmp in node_tmp.neighbours:
            if node_tmp == curr_node or len(node_min.neighbours_gate) > 0:
                node_min.neighbours.append(graphe_min[neighbour_tmp.id])
            elif neighbour_tmp.id == curr_node.id:
                node_min.neighbours.append(graphe_min[neighbour_tmp.id])

    return graphe_min


def find_min_dist(q, dist):
    min_dist = -1
    min_node = None

    for node_tmp in q:
        if min_dist == -1 or min_dist > dist[node_tmp]:
            min_dist = dist[node_tmp]
            min_node = node_tmp

    return min_node, min_dist


def dijkstra(graphe, node_start):
    q = []
    dist = dict()
    prev = dict()

    for node_tmp in graphe:
        dist[node_tmp] = math.inf
        prev[node_tmp] = None
        q.append(node_tmp)

    dist[node_start] = 0

    while q:
        u, min_dist = find_min_dist(q, dist)

        if min_dist == math.inf:
            return dist, prev

        q.remove(u)

        for v in u.neighbours:
            alt = dist[u] + 1  # 1 = length from u to v
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def find_node_to_cut(curr_node, graphe):
    if len(curr_node.neighbours_gate) > 0:
        return curr_node, curr_node.neighbours_gate[0]

    graphe_minimize = minimize(graphe, curr_node)
    node_start_min = graphe_minimize[curr_node.id]
    dist_min, prev_min = dijkstra(graphe_minimize, node_start_min)

    node_priority = None
    gate_priority = None
    priority = -10
    for node_tmp, dist_tmp in dist_min.items():
        if dist_tmp != math.inf and len(node_tmp.neighbours_gate) >= 2:
            if priority == -10 or priority > dist_tmp - len(node_tmp.neighbours_gate):
                priority = dist_tmp - len(node_tmp.neighbours_gate)
                node_priority = node_tmp
                gate_priority = node_tmp.neighbours_gate[0]

    if priority == -10:
        for node_tmp, dist_tmp in dist_min.items():
            if len(node_tmp.neighbours_gate) >= 2:
                priority = 0
                node_priority = node_tmp
                gate_priority = node_tmp.neighbours_gate[0]

    if priority == -10:
        for node_tmp, dist_tmp in dist_min.items():
            if len(node_tmp.neighbours_gate) >= 1:
                node_priority = node_tmp
                gate_priority = node_tmp.neighbours_gate[0]

    node_priority = graphe[node_priority.id]
    gate_priority = graphe[gate_priority.id]
    return node_priority, gate_priority


def main():
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in input().split()]
    graphe = [Node(i) for i in range(n)]
    gateways = []
    for i in range(l):
        # n1: N1 and N2 defines a link between these nodes
        n1, n2 = [int(j) for j in input().split()]
        node1 = graphe[n1]
        node2 = graphe[n2]
        node1.add_neighbour(node2)
        node2.add_neighbour(node1)
    for i in range(e):
        ei = int(input())  # the index of a gateway node
        graphe[ei].set_gateway()
        gateways.append(graphe[ei])
    # game loop
    while True:
        si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

        node_to_rem_link, nearest_gateway = find_node_to_cut(graphe[si], graphe)

        print(nearest_gateway.id, node_to_rem_link.id)
        nearest_gateway.remove_neighbour(node_to_rem_link)
        node_to_rem_link.remove_neighbour(nearest_gateway)


main()
