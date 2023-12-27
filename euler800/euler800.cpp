#include <iostream>
#include <cmath>
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



int largest_q(int p, double log_M) {
    // find the largest integer value for q such that
    //       p^q * q^p <= M
    // via binary search

    // Upper Bound(s)
    //       q <= log_p(M)      (tighter)
    //       q <= M^(1/p)

    // Lower Bound
    //       q >= 0


    double LB = 0.0;
    double UB = log_M / log(p);

    while (UB - LB > 1.0) {
        double q = (LB + UB) / 2;

        if (q*log(p) + p*log(q) <= log_M) {
            LB = q;
        } else {
            UB = q;
        }

    }

    // do a linear search about the convergence point to catch floating point inaccuracy 
    for (int q = LB - 3; q < UB + 3; q++) {
        if (q*log(p) + p*log(q) > log_M) {
            return q - 1;
        }
    }

    // return int(UB);
    return -1;
}



int main() {
    // double log_M = log(800);
    // double log_M = 800*log(800);
    double log_M = 800800*log(800800);

    int sieve_max = largest_q(2, log_M) + 1;
    cout << "sieve max: " << sieve_max << endl;
    bool* sieve = new bool[sieve_max];

    sieve_of_eratosthenes(sieve, sieve_max);
    cout << "sieve done" << endl;

    int* prime_counts = new int[sieve_max];     // primes_counts[n] gives # of primes <= n
    int c = 0;
    for (int n = 0; n < sieve_max; n++) {
        if (sieve[n]) c++;
        prime_counts[n] = c;
    }

    int count = 0;

    // count all pairs p < q satisfying p^q * q^p <= M
    for (int p = 0; p < sieve_max; p++) {
        if (!sieve[p]) continue;

        int q_max = largest_q(p, log_M);

        if (q_max > p) {
            count += prime_counts[q_max] - prime_counts[p];
        }
    }

    cout << count << endl;
}

// 1412403576
