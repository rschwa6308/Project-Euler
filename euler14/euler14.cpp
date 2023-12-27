#include <iostream>
using namespace std;


int collatz_length(int n_) {
    long n = n_;    // sequence may grow beyond int limit of 2^31

    int step_count = 0;
    while (n != 1) {
        // Collatz rule
        if (n % 2 == 0) {
            n = n/2;
        } else {
            n = 3*n + 1;
        }

        step_count++;
    }
    return step_count;
}


int main() {
    int max_length = -1;
    int best_n = -1;

    for (int n = 1; n < 1000000; n++) {
        int len = collatz_length(n);
        if (len > max_length) {
            max_length = len;
            best_n = n;
        }
    }

    cout << best_n << endl;

}