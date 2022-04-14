#include <iostream>
using namespace std;

int main() {
    int total = 0;
    for (int n = 1; n < 1000; n++) {
        if (n % 3 == 0 || n % 5 == 0) {
            total += n;
        }
    }
    cout << total;
}

// 233168
