#include <iostream>
#include <cmath>
#include <assert.h>


bool area_is_integer(long long a, long long b) {
    long long val = 4*a*a - b*b;
    long long root = sqrt(val);
    return root * root == val;
}




void euler94() {
    assert(area_is_integer(5, 6));

    const long long perimter_max = 1000000000;    // 1 billion

    long long total = 0;

    for (long long a = 3; a < perimter_max/3; a++) {
        for (long long b : {a - 1, a + 1}) {
            if (area_is_integer(a, b)) {
                // std::cout << a << " " << b << std::endl;
                total += a + a + b;
            }
        }
    }

    std::cout << total << std::endl;

}


#include "../helpers/timing.cpp"
int main() {
    auto duration = func_time_ms(euler94);
    std::cout << "\n(" << duration << " ms)" << std::endl;
}

// 518408346
