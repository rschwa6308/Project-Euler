#include <iostream>
#include <cmath>
using namespace std;


bool is_prime(int n) {
    for (int d = 2; d <= sqrt(n); d++) {
        if (n % d == 0) {
            return false;
        }
    }
    return true;
}


int smallest_pandivisible(int N) {
    // smallest positive integer divisible by 1 through N

    int res = 1;

    for (int n = 2; n <= N; n++) {
        if (!is_prime(n)) {continue;}
        int e = floor(log(N) / log(n));
        res *= pow(n, e);
    }

    return res;
}


int main() {
    cout << smallest_pandivisible(20);
}

// 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
// 232792560
