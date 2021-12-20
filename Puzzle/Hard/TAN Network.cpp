#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
#include <cmath>
#include <limits>

using namespace std;
class Node {
    public:
        string id;
        int id_nb;
        string name;
        double lon;
        double lat;
        vector<tuple<Node*, double>> neighbours;

        Node(string id, string name, double lat, double lon, int id_int) {
            this->id = id;
            this->id_nb = id_int;
            this->name = name;
            this->lat = lat * 0.0174533;
            this->lon = lon * 0.0174533;
        }

        void add_neighoubr(Node* new_node) {
            double x = (new_node->lon - lon) * cos((lat + new_node->lat) / 2);
            double y = (new_node->lat - lat);
            double d = sqrt(x * x + y * y) * 6371;

            neighbours.emplace_back(new_node, d);
        }

        bool has_neighbour(int id_other, Node*& neighbour) {
            for (auto const& node_dist : neighbours) {
                Node* node = get<0>(node_dist);
                if (node->id_nb == id_other) {
                    neighbour = node;
                    return true;
                }
            }
            return false;
        }

        double get_dist(int id_other) {
            for (auto const& node_dist : neighbours) {
                Node* node = get<0>(node_dist);
                double dist = get<1>(node_dist);
                if (node->id_nb == id_other) {
                    return dist;
                }
            }
            return -1.;
        }
};

Node* find_node(string id, vector<Node*> nodes) {
    for (auto const& node : nodes) {
        if (node->id == id) {
            return node;
        }
    }

    return nullptr;
}

vector<Node*> dijkstra(vector<Node*> graphe, Node* start) {
    vector<Node*> p;
    vector<Node*> remain;
    vector<double> d;
    vector<Node*> pred;

    for (auto const& node : graphe) {
        d.push_back(std::numeric_limits<double>::max());
        pred.push_back(nullptr);
        remain.push_back(node);
    }
    d[start->id_nb] = 0;

    while(!remain.empty()){
        // Find nearest vertex;
        double min_dist = std::numeric_limits<double>::max();
        Node* next_node = remain[0];
        int index = 0;
        int index_min = 0;
        for (auto const& node : remain) {
            if (d[node->id_nb] < min_dist) {
                min_dist = d[node->id_nb];
                next_node = node;
                index_min = index;
            }
            index++;
        }
        remain.erase(remain.begin() + index_min);

        // Compute new distances
        p.push_back(next_node);
        Node* neighbour;
        for (auto const& node : remain) {
            if (next_node->has_neighbour(node->id_nb, neighbour)) {
                double dist_neighbour = next_node->get_dist((node->id_nb));
                if (d[neighbour->id_nb] > d[next_node->id_nb] + dist_neighbour) {
                    d[neighbour->id_nb] = d[next_node->id_nb] + dist_neighbour;
                    pred[neighbour->id_nb] = next_node;
                }
            }
            index++;
        }
    }

    return pred;
}

int main()
{
    string start_point;
    cin >> start_point; cin.ignore();
    string end_point;
    cin >> end_point; cin.ignore();

    // Add all nodes
    int n;
    cin >> n; cin.ignore();

    vector<Node*> nodes;

    for (int i = 0; i < n; i++) {
        string stop_name;
        getline(cin, stop_name);

        string node_id;
        string node_name;
        double node_lat;
        double node_lon;

        // Split the string
        std::string delimiter = ",";
        int curr_index_word = 0;
        size_t pos = 0;
        std::string token;

        while ((pos = stop_name.find(delimiter)) != std::string::npos && curr_index_word < 5) {
            token = stop_name.substr(0, pos);

            switch(curr_index_word){
                case 0:
                    node_id = token;
                    break;
                case 1:
                    node_name = token;
                    break;
                case 3:
                    node_lat = stod(token);
                    break;
                case 4:
                    node_lon = stod(token);
                    break;
                default:
                    break;
            }
            stop_name.erase(0, pos + delimiter.length());
            curr_index_word++;
        }

        Node* new_node = new Node(node_id, node_name, node_lat, node_lon, i);
        nodes.push_back(new_node);
    }

    Node* node_start;
    Node* node_end;
    for (auto const& node : nodes) {
        if (node->id == start_point) {
            node_start = node;
        }
        if (node->id == end_point) {
            node_end = node;
        }
    }

    // Add all edges
    int m;
    cin >> m; cin.ignore();
    for (int i = 0; i < m; i++) {
        // Split string
        string node_id1;
        string node_id2;

        string route;
        getline(cin, route);
        std::string delimiter = " ";
        size_t pos = 0;
        std::string token;
        while ((pos = route.find(delimiter)) != std::string::npos) {
            token = route.substr(0, pos);
            node_id1 = token;
            route.erase(0, pos + delimiter.length());
        }
        node_id2 = route;

        // Add the edge
        Node* node1 = find_node(node_id1, nodes);
        Node* node2 = find_node(node_id2, nodes);

        node1->add_neighoubr(node2);
    }

    vector<Node*> pred = dijkstra(nodes, node_start);

    vector<string> path;
    Node* curr_node = node_end;

    while (pred[curr_node->id_nb] != nullptr && curr_node != node_start) {
        path.push_back(pred[curr_node->id_nb]->name);
        curr_node = pred[curr_node->id_nb];
    }

    if (pred[curr_node->id_nb] == nullptr && curr_node != node_start) {
    cout << "IMPOSSIBLE" << endl;
    }
    else {
        for (int k = path.size() - 1; k >= 0; k--) {
            string name = path[k];
            cout << name.substr(1, name.size() - 2) << endl;
        }
        cout << node_end->name.substr(1, node_end->name.size() - 2) << endl;
    }

}