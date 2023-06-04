#include <iostream>
#include <cmath>

void euler9() {
    const int N = 1000;
    for (int a = 1; a < N; a++) {
        for (int b = a; b < N; b++) {
            int c = N - (a + b);
            if (a*a + b*b == c*c) {
                std::cout << a*b*c << std::endl;
            }
        }
    }

}


#include "../helpers/timing.cpp"
int main() {
    auto duration = func_time_ms(euler9);
    std::cout << "\n(" << duration << " ms)" << std::endl;
}
