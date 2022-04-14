#include <iostream>
#include <cmath>
using namespace std;


bool is_palindrome(int n) {
    int len = ceil(log10(n));
    int digits [len];

    for (int i = 0; i < len; i++) {
        digits[i] = n % 10;
        n /= 10;
    }

    for (int i = 0; i <= len/2; i++) {
        if (digits[i] != digits[len - i - 1]) {
            return false;
        }
    }

    return true;

}


int main() {
    int largest_palindrome = -1;

    for (int a = 100; a <= 998; a++) {
        for (int b = a+1; b <= 999; b++) {
            int n = a * b;
            if (n > largest_palindrome && is_palindrome(n)) {
                cout << n << endl;
                largest_palindrome = n;
            }
        }
    }

    cout << largest_palindrome;
}

// 906609
