#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>


bool is_square(long long N) {
    long long r = round(sqrt(N));
    return r*r == N;
}

bool is_prime(long long n) {
    if (n%2 == 0) return false;
    for (long long d = 3; d < sqrt(n); d+=2) {
        if (n%d == 0) {
            return false;
        }
    }

    return true;
}


long long reverse(long long n) {
    std::string s = std::to_string(n);
    std::reverse(s.begin(), s.end());
    return std::stoll(s);
}


void euler808() {
    long long total = 0;
    int num_found = 0;
    for (long long n = 1; num_found < 50; n+=2) {
        long long N = n*n;

        if (N%10 != 1 && N%10 != 9) continue;

        long long N_rev = reverse(N);

        if (N == N_rev) continue;

        if (!is_square(N_rev)) continue;

        long long n_rev =  round(sqrt(N_rev));

        if (is_prime(n) && is_prime(n_rev)) {
            std::cout << N << std::endl;

            num_found++;
            total += N;
        }
    }

    std::cout << total << std::endl;
}

#include "../helpers/timing.cpp"
int main() {
    auto duration = func_time_ms(euler808);
    std::cout << "\n(" << duration << " ms)" << std::endl;
}
