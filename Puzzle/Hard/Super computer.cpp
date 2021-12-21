#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool sortbysec(const pair<int,int> &a, const pair<int,int> &b)
{
    return (a.second < b.second);
}

int main()
{
    vector<bool> used(1000000, false);
    vector<pair<int, int>> calculations;  // start, end
    int nb_calculations = 0;

    int n;
    cin >> n; cin.ignore();

    for (int i = 0; i < n; i++) {
        int j;
        int d;
        cin >> j >> d; cin.ignore();
        calculations.emplace_back(j, j + d - 1);
    }

    sort(calculations.begin(), calculations.end(), sortbysec);
    pair<int, int> last_calculation = {-1, -1};
    for (auto const &calculation : calculations) {
        if (calculation.first > last_calculation.second) {
            last_calculation = calculation;
            nb_calculations++;
        }
    }

    cout << nb_calculations << endl;
}