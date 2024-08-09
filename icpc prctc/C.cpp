#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> heights(n), costs(n);

    for (int i = 0; i < n; i++) {
        cin >> heights[i] >> costs[i];
    }

    int totalCost = 0;

    for (int i = 1; i < n; i++) {
        if (heights[i] <= heights[i - 1]) {
            int neededHeight = heights[i - 1] - heights[i] + 1;
            totalCost += neededHeight * costs[i];
            heights[i] += neededHeight;
        }
    }

    cout << totalCost << endl;

    return 0;
}