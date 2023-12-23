#include <iostream>
using namespace std;


void sieve_of_eratosthenes(bool* sieve, int sieve_max) {
    // set all values to true (except for 0 and 1)
    sieve[0] = false;
    sieve[1] = false;
    for (int i = 2; i <= sieve_max; i++) {
        sieve[i] = true;
    }

    // sieve algorithm
    int p = 2;
    while (p*p < sieve_max) {
        // find next prime
        while (!sieve[p]) {
            p++;
        }

        // mark out all multiples of p, starting from p^2
        for (int i = p*p; i <= sieve_max; i += p) {
            sieve[i] = false;
        }

        p++;
    }
}


int main() {
    int sieve_max = 2000000;
    // int sieve_max = 101;
    bool sieve[sieve_max];

    sieve_of_eratosthenes(sieve, sieve_max);

    long total = 0;
    for (int i = 2; i < sieve_max; i++) {
        // cout << i << " " << sieve[i] << endl;
        if (sieve[i]) {
            total += i;
        }
    }

    cout << total << endl;
}

// 142913828922
