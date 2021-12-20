import math
import random
import heapq
from enum import Enum


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a.i, a.j
    (x2, y2) = b.i, b.j
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {start: 0}
    came_from[start] = None
    goal_found = False
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            goal_found = True

        for next_neighbour in current.neighbours:
            new_cost = cost_so_far[current] + 1
            if next_neighbour not in cost_so_far or new_cost < cost_so_far[next_neighbour]:
                cost_so_far[next_neighbour] = new_cost
                priority = new_cost + heuristic(next_neighbour, goal)
                frontier.put(next_neighbour, priority)
                came_from[next_neighbour] = current
                if next_neighbour == goal:
                    return cost_so_far, came_from, True

    return cost_so_far, came_from, goal_found


class Type(Enum):
    UNKNOWN = "?"
    BLOCK = "#"
    FREE = "."


class NodeTree:
    def __init__(self, i, j, parent=None):
        self.i = i
        self.j = j
        self.parent = parent
        self.childs = []


class Node:
    id_max = 0

    def __init__(self, type_case=Type.UNKNOWN, i=0, j=0):
        self.type = type_case
        self.neighbours = []
        self.chara = "?"
        self.unknown_neighbours = []
        self.id = Node.id_max
        self.i = i
        self.j = j
        self.cout = 10
        self.heuristique = 10
        Node.id_max += 1

    def add_neighbour(self, node2):
        """
        Add node2 as a neighbour of this node only if this node type is free
        and node2 type is also free.
        """
        if self.type != Type.FREE:
            return

        if node2.chara == "?":
            self.unknown_neighbours.append(node2)
        else:
            self.neighbours.append(node2)

    def set_chara(self, char):
        if self.chara == "?":
            self.chara = char

    def __lt__(self, other):
        if self.heuristique < other.heuristique:
            return True
        if self.heuristique == other.heuristique:
            return False
        return False

    def __hash__(self):
        return self.id

    def __str__(self):
        return "(" + str(self.id) + ", " + str(self.type) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id


def update_matrix(matrix_type, matrix_node, i, j, char):
    matrix_type[i][j] = char
    curr_node = matrix_node[i][j]
    curr_node.i = i
    curr_node.j = j
    curr_node.set_chara(char)
    if char == "#":
        curr_node.type = Type.BLOCK
    else:
        curr_node.type = Type.FREE

        if i > 0:  # north
            matrix_node[i - 1][j].add_neighbour(curr_node)
            curr_node.add_neighbour(matrix_node[i - 1][j])

        if i < len(matrix_node) - 1:  # south
            matrix_node[i + 1][j].add_neighbour(curr_node)
            curr_node.add_neighbour(matrix_node[i + 1][j])

        if j > 0:  # west
            matrix_node[i][j - 1].add_neighbour(curr_node)
            curr_node.add_neighbour(matrix_node[i][j - 1])

        if j < len(matrix_node[0]) - 1:  # east
            matrix_node[i][j + 1].add_neighbour(curr_node)
            curr_node.add_neighbour(matrix_node[i][j + 1])


def find_min_dist(q, dist):
    min_dist = -1
    min_node = None
    for node_tmp in q:
        if min_dist == -1 or min_dist > dist[node_tmp]:
            min_dist = dist[node_tmp]
            min_node = node_tmp

    return min_node, min_dist


def random_dir(matrix_node, matrix_explored, matrix_type, kr, kc):
    directions = []
    if kr > 0 and matrix_explored[kr - 1][kc] is False and matrix_type[kr - 1][kc] == ".":
        directions.append("UP")

    if kr < len(matrix_explored) - 1 and matrix_explored[kr + 1][kc] is False and matrix_type[kr + 1][kc] == ".":
        directions.append("DOWN")

    if kc > 0 and matrix_explored[kr][kc - 1] is False and matrix_type[kr][kc - 1] == ".":  # west
        directions.append("LEFT")

    if kc < len(matrix_node[0]) - 1 and matrix_explored[kr][kc + 1] is False and matrix_type[kr][kc + 1] == ".":
        directions.append("RIGHT")

    if len(directions) > 0:
        return random.choice(directions)
    return None


def inverse_dir(direction):
    if direction == "UP":
        return "DOWN"
    elif direction == "DOWN":
        return "UP"
    elif direction == "RIGHT":
        return "LEFT"
    else:
        return "RIGHT"


def comparer(n1, n2):
    if n1.heuristique < n2.heuristique:
        return 1
    if n1.heuristique == n2.heuristique:
        return 0
    return -1


class FilePrio:
    def __init__(self, noeud):
        self.noeud = noeud
        self.suivant = None
        self.prec = None

    def est_vide(self):
        return self.noeud is None

    def insert(self, n2):
        if comparer(self.noeud, n2) == 1:
            if self.suivant:
                self.suivant.insert(n2)
            else:
                prev_next = self.suivant
                self.suivant = FilePrio(n2)
                self.suivant.suivant = prev_next
        else:
            new_noeud = FilePrio(n2)
            new_noeud.prec = self.prec
            new_noeud.suivant = self

            self.prec.suivant = new_noeud
            self.prec = new_noeud

    def defiler(self):
        if self.suivant is not None:
            prev_next = self.suivant.prec = None
        else:
            prev_next = None
        return self, prev_next


def dijkstra(matrix_node, extended, kr, kc, end_node=None):
    graphe = []
    node_start = matrix_node[kr][kc]
    for row in matrix_node:
        for node_tmp in row:
            graphe.append(node_tmp)

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

        if extended:
            u_neighbours = u.neighbours + u.unknown_neighbours
        else:
            u_neighbours = u.neighbours

        for v in u_neighbours:
            if v in q and v.type != Type.BLOCK:

                alt = dist[u] + 1  # 1 = length from u to v
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        if end_node and u == end_node:
            return dist, prev
    return dist, prev


def go_to_node(matrix_node, kr, kc, new_node, r):
    if kr > 0 and matrix_node[kr - 1][kc] == new_node:
        print("UP")
    elif kr < r - 2 and matrix_node[kr + 1][kc] == new_node:
        print("DOWN")
    elif kc > 0 and matrix_node[kr][kc - 1] == new_node:
        print("LEFT")
    else:
        print("RIGHT")


def main():
    r, c, a = [int(i) for i in input().split()]
    matrix_node = [[Node() for _ in range(c)] for _ in range(r)]
    matrix_type = [["#" for _ in range(c)] for _ in range(r)]
    matrix_explored = [[False for _ in range(c)] for _ in range(r)]
    goal_founded = False
    mouv_left = 1200
    path_to_end = None
    path_to_start = None
    going_to_goal = True
    calculate_path = False
    rec_liste = []
    node_end = None
    node_start = None
    dist_to_start = []

    # game loop
    while True:
        # kr: row where Kirk is located.
        # kc: column where Kirk is located.
        kr, kc = [int(i) for i in input().split()]
        for i in range(r):
            row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
            for j, chara in enumerate(row):
                if chara != "?" and matrix_type != "?":  # check if we haven't seen the case yet
                    update_matrix(matrix_type, matrix_node, i, j, chara)
                if chara == "T":
                    node_start = matrix_node[i][j]
                if chara == "C":
                    goal_founded = True
                    node_end = matrix_node[i][j]

        if calculate_path:
            dist1, prev1, _ = a_star_search(matrix_node[kr][kc], node_end)
            if dist1[node_end] + dist_to_start[node_start] > mouv_left:
                matrix_explored[kr][kc] = True
                next_dir = random_dir(matrix_node, matrix_explored, matrix_type, kr, kc)
                if next_dir is not None:
                    rec_liste.append(inverse_dir(next_dir))
                    print(next_dir)
                else:
                    print(rec_liste[-1])
                    rec_liste.pop()
            else:

                calculate_path = False
                path_to_end = prev1

        if not goal_founded:
            matrix_explored[kr][kc] = True
            next_dir = random_dir(matrix_node, matrix_explored, matrix_type, kr, kc)
            if next_dir is not None:
                rec_liste.append(inverse_dir(next_dir))
                print(next_dir)
            else:
                print(rec_liste[-1])
                rec_liste.pop()

        elif path_to_end is None:
            dist2, prev2, reachable = a_star_search(node_end, node_start)
            path_to_start = prev2
            dist_to_start = dist2
            if reachable:

                if dist2[node_start] > a:
                    matrix_explored[kr][kc] = True
                    next_dir = random_dir(matrix_node, matrix_explored, matrix_type, kr, kc)
                    if next_dir is not None:
                        rec_liste.append(inverse_dir(next_dir))
                        print(next_dir)
                    else:
                        print(rec_liste[-1])
                        rec_liste.pop()

                else:
                    matrix_explored[kr][kc] = True
                    next_dir = random_dir(matrix_node, matrix_explored, matrix_type, kr, kc)
                    if next_dir is not None:
                        rec_liste.append(inverse_dir(next_dir))
                        print(next_dir)
                    else:
                        print(rec_liste[-1])
                        rec_liste.pop()
                    calculate_path = True

            else:
                matrix_explored[kr][kc] = True
                next_dir = random_dir(matrix_node, matrix_explored, matrix_type, kr, kc)
                if next_dir is not None:
                    rec_liste.append(inverse_dir(next_dir))
                    print(next_dir)
                else:
                    print(rec_liste[-1])
                    rec_liste.pop()
            mouv_left -= 1

        if path_to_end is not None:
            # Here we have found the path !
            if going_to_goal:
                node_prev = node_end
                while path_to_end[node_prev] != matrix_node[kr][kc]:
                    node_prev = path_to_end[node_prev]
                go_to_node(matrix_node, kr, kc, node_prev, r)
                if node_prev.chara == "C":
                    going_to_goal = False
            else:
                node_prev = node_start
                while path_to_start[node_prev] != matrix_node[kr][kc]:
                    node_prev = path_to_start[node_prev]
                go_to_node(matrix_node, kr, kc, node_prev, r)


main()
