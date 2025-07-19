#include <array>
#include <cmath>


std::array<uint64_t, 20> POWERS_OF_TEN;


// Determine if N = s^2 is a '2025' number
bool is_2025(uint64_t s) {
    uint64_t N = s*s;

    int num_digits = int(log10(N)) + 1;

    uint64_t a, b;
    for (int i = 1; i < num_digits; i++) {
        a = N / POWERS_OF_TEN[i];
        b = N % POWERS_OF_TEN[i];

        if ((N / POWERS_OF_TEN[i-1]) % 10 == 0) { continue; }

        if (a + b == s) { return true; }
    }

    return false;
}


uint64_t T(int n) {
    uint64_t total = 0;

    for (uint64_t s = 1; s < POWERS_OF_TEN[n/2]; s++) {
        if (is_2025(s)) {
            total += s*s;
            printf("%llu\n", s*s);
        }
    }

    return total;
}


int main() {
    for (int i = 0; i < POWERS_OF_TEN.size(); i++) {
        POWERS_OF_TEN[i] = pow(10, i);
    }

    assert(is_2025(45));
    assert(!is_2025(99));

    printf("T(4) = %llu\n", T(4));
    assert(T(4) == 5131);
    
    printf("T(16) = %llu\n", T(16));
}


// T(16) = 72673459417881349 (in 16.4s)
