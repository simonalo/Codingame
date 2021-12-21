#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<vector<int>> visited;

// Algo of flood fill to see which cell belogn to which lake
// See https://en.wikipedia.org/wiki/Flood_fill
int flood_fill(int i, int j, vector<string> surface, int width, int height) {
    if (visited[i][j] != 0) {
        return visited[i][j];
    }

    // Inside : 2d vector
    vector<vector<bool>> inside(surface.size(), vector<bool>(surface[0].size(), true));
    int new_size = 0;
    vector<pair<int, int>> reached_nodes; // Update value of each cells after we have finished flood algo

    queue<pair<int, int>> q;
    q.push({i, j});

    while (!q.empty()) {
        pair<int, int> node = q.front();
        q.pop();

        int y = node.first;
        int x = node.second;

        if (inside[y][x] && surface[y][x] != '#') {
            new_size++;
            reached_nodes.push_back({y, x});
            inside[y][x] = false;

            // Fill others
            if (y < height - 1) {
                q.push({y + 1, x});
            }
            if (y > 0) {
                q.push({y - 1, x});
            }
            if (x > 0) {
                q.push({y, x - 1});
            }
            if (x < width - 1) {
                q.push({y, x + 1});
            }
        }
    }

    for (const pair<int,int> &node : reached_nodes )
    {
        visited[node.first][node.second] = new_size;
    }

    return new_size;
}

int main()
{
    // Get width and height
    int width;
    cin >> width; cin.ignore();
    int height;
    cin >> height; cin.ignore();

    // Get map
    vector<string> surface;

    for (int i = 0; i < height; i++) {
        string row;
        getline(cin, row);
        surface.push_back(row);
        visited.push_back({});
        for (int j = 0; j < width; j++) {
            visited.back().push_back(0);
        }
    }

    // Get coord where we want to know the size of the area
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int x;
        int y;
        cin >> x >> y; cin.ignore();

        if (surface[y][x] != '#') {
            if (visited[y][x] == 0) {
                int new_size = flood_fill(y, x, surface, width, height);
            }
            cout << visited[y][x] << endl;
        }
        else {
            cout << 0 << endl;
        }
    }
}