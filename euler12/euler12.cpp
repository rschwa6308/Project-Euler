#include <iostream>
#include <cmath>
using namespace std;


int count_divisors(int n) {
    int count = 0;

    int sqrt_n = sqrt(n);
    for (int i = 1; i <= sqrt_n; i++) {
        if (n % i == 0) {
            count += 2;     // count both i and N/i
        }
    }

    // if n is a perfect square, then we double counted sqrt(n)
    if (sqrt_n*sqrt_n == n) {
        count--;
    }

    return count;
}


int main() {
    int n = 0;

    for (int i = 1;; i++) {
        n += i;
        if (count_divisors(n) >= 500) {
            break;
        }
    }

    cout << n << endl;
}

// 76576500
