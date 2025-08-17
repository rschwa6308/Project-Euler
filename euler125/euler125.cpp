#include <cstdint>
#include <stddef.h>
#include <iostream>
#include <cmath>
#include <set>

constexpr size_t TABLE_SIZE = 4000;

// TABLE[i][j] = i^2 + ... + j^2
uint64_t CONSECUTIVE_SQUARE_SUMS_TABLE[TABLE_SIZE][TABLE_SIZE] = {0};



void populate_table() {
    std::cout << "Populating table... " << std::flush;

    for (uint64_t i = 0; i < TABLE_SIZE; i++) {
        CONSECUTIVE_SQUARE_SUMS_TABLE[i][i] = i*i;
        for (uint64_t j = i+1; j < TABLE_SIZE; j++) {
            CONSECUTIVE_SQUARE_SUMS_TABLE[i][j] = CONSECUTIVE_SQUARE_SUMS_TABLE[i][j-1] + j*j;
        }
    }

    std::cout << "done" << std::endl;

    // // print table
    // for (int i = 0; i < TABLE_SIZE; i++) {
    //     for (int j = 0; j < TABLE_SIZE; j++) {
    //         std::cout << CONSECUTIVE_SQUARE_SUMS_TABLE[i][j] << " ";
    //     }
    //     std::cout << std::endl;
    // }

}


bool is_palindrome(uint64_t n) {
    uint64_t rev = 0, orig = n;
    while (n > 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev == orig;
}



// solutions can appear multiple times - maintain a unique set
std::set<uint64_t> solutions;


uint64_t MAX = 1e8;

int main() {
    assert(is_palindrome(1234321));
    assert(!is_palindrome(12354657));

    populate_table();

    assert(CONSECUTIVE_SQUARE_SUMS_TABLE[5][8] == 5*5 + 6*6 + 7*7 + 8*8);

    for (int i = 1; i < TABLE_SIZE-1; i++) {
        for (int j = i+1; j < TABLE_SIZE; j++) {
            uint64_t n = CONSECUTIVE_SQUARE_SUMS_TABLE[i][j];
            if (n >= MAX) { continue; }
            if (is_palindrome(n)) {
                solutions.emplace(n);
            }
        }
    }

    uint64_t total = 0;
    for (const auto& n : solutions) {
        total += n;
    }

    std::cout << total << std::endl;
}

// => 2906969179 (in 85ms)
