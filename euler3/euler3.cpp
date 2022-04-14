#include <iostream>
#include <cmath>
using namespace std;


long long largest_prime_factor(long long n) {
    // int largest_factor = -1;
    bool prime = false;
    while (!prime) {
        prime = true;
        // cout << n << endl;
        for (int d = 2; d < sqrt(n); d++) {
            if (n % d == 0) {
                // cout << d << endl;
                prime = false;
                n = n/d;
                break;
            }
        }
    }

    return n;
}


int main() {
    cout << largest_prime_factor(600851475143L);
}

// 6857
