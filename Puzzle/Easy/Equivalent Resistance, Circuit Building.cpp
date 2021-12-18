#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include<sstream>

using namespace std;

class Node {
    public:
        int cout;
        int operation; // 0 pour série et 1 pour parallèle et -1 pour une lettre
        vector<Node*> childs = vector<Node*>();
        Node* parent;

        Node(int cout, int operation, Node* parent) {
            this->cout = cout;
            this->operation = operation;
            this->parent = parent;
        }

        double calcul() {
            // On vérifie si c'est une feuille (i.e. une lettre avec un coût)
            if (cout != -1)
            {
                return static_cast<double>(cout);
            }

            double result = 0.0;
            for (Node* child : childs)
            {
                //cerr << child->cout << endl;
                if (operation == 0)
                {
                    result += child->calcul();
                }
                else
                {
                    result += 1. / child->calcul();
                }
            }
            cerr << (this->operation == 0 ? result : 1 / result) << endl;
            return this->operation == 0 ? result : 1 / result;
        }
};

int find_cout(string lettre, vector<pair<string, int>> couts_lettre)
{
    for (auto& cout : couts_lettre)
    {
        //cerr << cout.first << cout.second << lettre << endl;
        if (cout.first == lettre)
        {
            return cout.second;
        }
    }

    return -1;
}

vector<string> split(const string &s, char delim) {
        vector<string> elems;
        stringstream ss(s);
        string item;
        while (getline(ss, item, delim)) {
            elems.push_back(item);
        }
        return elems;
    }

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    vector<pair<string, int>> couts_lettre;
    Node* first_node = new Node(-1, -1, nullptr);
    Node* curr_node = first_node;

    int n;
    cin >> n; cin.ignore();

    for (int i = 0; i < n; i++) {
        string name;
        int r;
        cin >> name >> r; cin.ignore();
        // cerr << name << r << endl;
        couts_lettre.emplace_back(name, r);
    }

    string circuit;
    getline(cin, circuit);
    vector<string> x = split(circuit,' ');

    for (string curr_string : x)
    {
        if (curr_string == " ")
        {
            // On ne fait rien
        }
        else if (curr_string == "(")
        {
            Node* new_child = new Node(-1, 0, curr_node);
            curr_node->childs.push_back(new_child);
            curr_node = new_child;

        }
        else if (curr_string == "[")
        {
            Node* new_child = new Node(-1, 1, curr_node);
            curr_node->childs.push_back(new_child);
            curr_node = new_child;
        }
        else if (curr_string == "]" || curr_string == ")")
        {
            if (curr_node->parent != nullptr)
            {
                curr_node = curr_node->parent;
            }
        }
        else
        {
            // C'est une lettre
            double cout = find_cout(curr_string, couts_lettre);
            //cerr << cout << endl;
            Node* new_child = new Node(cout, -1, curr_node);
            curr_node->childs.push_back(new_child);
        }
    }


    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    printf("%.1f", round(first_node->calcul() * 1000) / 1000);
}