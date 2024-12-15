#include <iostream>
#include <vector>

int main() {
    std::vector<int> num;

    for (int i=0; i<10; i++) {
        num.push_back(i+10);

    }

    for (int i: num) {
        std::cout << i << " ";
    }

    return 0;
}