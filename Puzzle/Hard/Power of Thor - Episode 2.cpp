#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <tuple>

using namespace std;

bool is_dangerous(int x, int y, vector<tuple<int, int>> giants_pos)
{
    for (auto const& giant_pos : giants_pos) {
        int x_giant = get<0>(giant_pos);
        int y_giant = get<1>(giant_pos);
        if (abs(x - x_giant) <= 1 && abs(y - y_giant) <= 1) {
            return true;
        }
    }
    return false;
}

vector<tuple<int, int, string>> create_moves(int thor_x, int thor_y)
{
    vector<tuple<int, int, string>> moves;

    if (thor_y > 0)
        moves.emplace_back(thor_x + 0, thor_y - 1, "N");
    if (thor_y > 0 && thor_x < 39)
        moves.emplace_back(thor_x + 1, thor_y - 1, "NE");
    if (thor_x < 39)
        moves.emplace_back(thor_x + 1, thor_y + 0, "E");
    if (thor_y < 17 && thor_x < 39)
        moves.emplace_back(thor_x + 1, thor_y + 1, "SE");
    if (thor_y < 17)
        moves.emplace_back(thor_x + 0, thor_y + 1, "S");
    if (thor_x > 0 && thor_y < 17)
        moves.emplace_back(thor_x - 1, thor_y + 1, "SW");
    if (thor_x > 0)
        moves.emplace_back(thor_x - 1, thor_y + 0, "W");
    if (thor_y > 0 && thor_x > 0)
        moves.emplace_back(thor_x - 1, thor_y - 1, "NW");

    return moves;
}

bool closer(tuple<int, int, string> move1, tuple<int, int, string> move2, int target_x, int target_y)
{
    int x1 = get<0>(move1);
    int y1 = get<1>(move1);
    int x2 = get<0>(move2);
    int y2 = get<1>(move2);

    float dist1 = sqrt(((target_x - x1) * (target_x - x1) + (target_y - y1) * (target_y - y1)));
    float dist2 = sqrt(((target_x - x2) * (target_x - x2) + (target_y - y2) * (target_y - y2)));

    return dist1 < dist2;
}

void sort_moves(vector<tuple<int, int, string>>& moves, int target_x, int target_y)
{
    for (int i = 0; i < moves.size(); ++i) {
        tuple<int, int, string> move = moves[i];
        int j = i;
        while(j > 0 && closer(move, moves[j - 1], target_x, target_y)){
            moves[j] = moves [j - 1];
            j--;
        }

        moves[j] = move;
    }
}

void find_next_pos(vector<tuple<int, int> > giants_pos, int& thor_x, int& thor_y, int& next_x, int& next_y, string& next_move, int center_x, int center_y)
{
    vector<tuple<int, int, string>> moves = create_moves(thor_x, thor_y);
    sort_moves(moves, center_x, center_y);

    int i = 0;
    bool strike = false;
    while (is_dangerous(get<0>(moves[i]), get<1>(moves[i]), giants_pos)) {
        i += 1;
        if (i == moves.size()) {
            strike = true;
            break;
        }
    }

    if (strike) {
        next_x = thor_x;
        next_y = thor_y;
        next_move = "STRIKE";
    }
    else {
        next_x = get<0>(moves[i]);
        next_y = get<1>(moves[i]);
        if (next_x == thor_x && next_y == thor_y) {
            next_move = "WAIT";
        }
        else {
            next_move = get<2>(moves[i]);
        }
    }
}

int main()
{
    int thor_x;
    int thor_y;
    cin >> thor_x >> thor_y; cin.ignore();
    int go_diag = 0;
    vector<tuple<int, int>> giants_pos;
    while (1) {
        giants_pos.clear();
        int min_x = 40;
        int max_x = 0;
        int min_y = 40;
        int max_y = 0;
        int hammer; // the remaining number of hammer strikes.
        int nb_giants; // the number of giants which are still present on the map.
        cin >> hammer >> nb_giants; cin.ignore();
        for (int i = 0; i < nb_giants; i++) {
            int x;
            int y;
            cin >> x >> y; cin.ignore();
            giants_pos.emplace_back(x, y);

            if (min_x > x) {
                min_x = x;
            }
            if (max_x < x) {
                max_x = x;
            }
            if (min_y > y) {
                min_y = y;
            }
            if (max_y < y) {
                max_y = y;
            }
        }

        int center_x = floor((min_x + max_x) / 2);
        int center_y = floor((min_y + max_y) / 2);

        int next_x = thor_x, next_y = thor_y;
        string next_mouv = "";
        find_next_pos(giants_pos, thor_x, thor_y, next_x, next_y, next_mouv, center_x, center_y);
        bool test = go_diag == 0;
        if ((min_x != max_x && min_y != max_y && go_diag == 0) || nb_giants == 1) {
            cout << next_mouv << endl;

            thor_x = next_x;
            thor_y = next_y;
        } else if (min_y == max_y) {
            if (!(min_y == max_y)) {
                go_diag--;
            }
            else {
                go_diag = 1;
            }
            next_mouv = "";
            next_x = thor_x;
            next_y = thor_y;
            find_next_pos(giants_pos, thor_x, thor_y, next_x, next_y, next_mouv, center_x, 16);

            cout << next_mouv << endl;

            thor_x = next_x;
            thor_y = next_y;
        }  else if (min_x == max_x) {
            if (!(min_x == max_x)) {
                go_diag--;
            }
            else {
                go_diag = 1;
            }
            next_mouv = "";
            next_x = thor_x;
            next_y = thor_y;

            find_next_pos(giants_pos, thor_x, thor_y, next_x, next_y, next_mouv, 0, center_y);

            cout << next_mouv << endl;

            thor_x = next_x;
            thor_y = next_y;
        } else {
            go_diag--;
            next_mouv = "";
            next_x = thor_x;
            next_y = thor_y;

            find_next_pos(giants_pos, thor_x, thor_y, next_x, next_y, next_mouv, center_x, 17);

            cout << next_mouv << endl;

            thor_x = next_x;
            thor_y = next_y;
        }

    }
}