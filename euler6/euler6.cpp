#include <iostream>
#include <cmath>


int sum_of_squares(int N) {
    int sum = 0;
    for (int n = 1; n <= N; n++) {
        sum += n * n;
    }
    return sum;
}


int sum_of_squares_fast(int N) {
    // https://en.wikipedia.org/wiki/Faulhaber%27s_formula
    return N * (N+1) * (2*N+1) / 6;
}


int square_of_sum(int N) {
    int sum = 0;
    for (int n = 1; n <= N; n++) {
        sum += n;
    }
    return sum * sum;
}


int square_of_sum_fast(int N) {
    // https://en.wikipedia.org/wiki/Faulhaber%27s_formula
    int sum = N * (N+1) / 2;
    return sum * sum;
}




void euler6() {
    // std::cout << square_of_sum(100) - sum_of_squares(100);
    std::cout << square_of_sum_fast(100) - sum_of_squares_fast(100) << std::endl;
}


#include "../helpers/timing.cpp"
int main() {
    auto duration = func_time_ns(euler6);
    std::cout << "\n(" << duration << " ns)" << std::endl;
}


// 25164150
