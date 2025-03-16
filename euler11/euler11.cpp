#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;



int main() {
    int GRID[20][20];

    // parse grid from file
    ifstream input_file;
    input_file.open("input.txt");

    string line;
    for (int i = 0; i < 20; i++) {
        getline(input_file, line);
        stringstream line_ss(line);

        for (int j = 0; j < 20; j++) {
            string num;
            getline(line_ss, num, ' ');
            GRID[i][j] = stoi(num);
        }
    }
    
    input_file.close();

    int max_product = -1;

    // search horizontally
    for (int y = 0; y < 20; y++) {
        for (int x = 0; x < 20-4; x++) {
            int prod = GRID[y][x] * GRID[y][x+1] * GRID[y][x+2] * GRID[y][x+3];
            max_product = max(max_product, prod);
        }
    }

    // search vertically
    for (int y = 0; y < 20-4; y++) {
        for (int x = 0; x < 20; x++) {
            int prod = GRID[y][x] * GRID[y+1][x] * GRID[y+2][x] * GRID[y+3][x];
            max_product = max(max_product, prod);
        }
    }

    // search diagonally down (\)
    for (int y = 0; y < 20-4; y++) {
        for (int x = 0; x < 20-4; x++) {
            int prod = GRID[y][x] * GRID[y+1][x+1] * GRID[y+2][x+2] * GRID[y+2][x+2];
            max_product = max(max_product, prod);
        }
    }

    // search diagonally up (/)
    for (int y = 4; y < 20; y++) {
        for (int x = 0; x < 20-4; x++) {
            int prod = GRID[y][x] * GRID[y-1][x+1] * GRID[y-2][x+2] * GRID[y-3][x+3];
            max_product = max(max_product, prod);
        }
    }

    cout << max_product << endl;
}


// 70600674
