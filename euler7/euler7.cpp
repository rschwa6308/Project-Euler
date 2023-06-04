#include <iostream>
#include <cmath>

// TODO: sieve method

bool is_prime(int n) {
    for (int d = 2; d <= (int)sqrt(n); d++) {
        if (n%d == 0) {
            return false;
        }
    }
    return true;
}


void euler7() {
    int prime_count = 0;
    int n;
    for (n = 2; prime_count < 10001; n++) {
        if (is_prime(n)) {
            // std::cout << n << std::endl;
            prime_count++;
        }
    }
    std::cout << n-1 << std::endl;
}


#include "../helpers/timing.cpp"
int main() {
    auto duration = func_time_ms(euler7);
    std::cout << "\n(" << duration << " ms)" << std::endl;
}
