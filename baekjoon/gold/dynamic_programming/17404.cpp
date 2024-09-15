#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;
typedef tuple<int, int, int> Cost;
typedef vector<Cost> Data;
enum position {
    R, G, B
};

int calc_price(const Data& data, enum position starting_position);


// // debug
// ostream& operator<<(ostream& out, const Cost& c) { 
//    out << "R = " << get<0>(c) << ", G = " << get<1>(c) << ", B = " << get<2>(c);
//    return out;
// }

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    Data data;
    data.reserve(N);
    for (int i = 0; i < N; i++){
        int pr, pg, pb;
        cin >> pr >> pg >> pb;
        data.push_back(Cost(pr, pb, pg));
    }
    cout << min({calc_price(data, R), calc_price(data, G), calc_price(data, B)}) << endl;
}

int calc_price(const Data& data, enum position starting_position) {
    Cost current_costs;
    switch (starting_position) {
    case R:
        current_costs = {1000 * 1000, get<0>(data[0]) + get<1>(data[1]),  get<0>(data[0]) + get<2>(data[1])};
        break;
    case G:
        current_costs = {get<1>(data[0]) + get<0>(data[1]),  1000 * 1000, get<1>(data[0]) + get<2>(data[1])};
        break;
    case B:
        current_costs = {get<2>(data[0]) + get<0>(data[1]),  get<2>(data[0]) + get<1>(data[1]), 1000 * 1000};
        break;
    default:
    throw 1;
    }

    for (auto it = data.begin() + 2; it != data.end(); it++) {
        const Cost cost = *it;
        Cost new_costs = {
            min(get<1>(current_costs), get<2>(current_costs)) + get<0>(cost),
            min(get<0>(current_costs), get<2>(current_costs)) + get<1>(cost),
            min(get<0>(current_costs), get<1>(current_costs)) + get<2>(cost),
        };
        current_costs = new_costs;
    }
    switch (starting_position) {
    case R:
        return min({get<1>(current_costs), get<2>(current_costs)});
    case G:
        return min({get<0>(current_costs), get<2>(current_costs)});
    case B:
        return min({get<0>(current_costs), get<1>(current_costs)});
    }
}
