#include <iostream>
using namespace std;

int main() {
    int total = 0;

    int a = 1;
    int b = 2;
    while (a <= 4000000) {
        if (a % 2 == 0) {
            total += a;
        }
        int temp = a;
        a = b;
        b += temp;
    }
    cout << total;
}

// 4613732
