#include <iostream>
#include <string>

int main() {
    int x = 25;
    int y = 30;

    bool igual = x == y;
    bool diferente = x != y;
    bool maior = x > y;
    bool menor_igual = x <= y;

    std::cout << "x == y: " << igual << std::endl;
    std::cout << "x != y: " << diferente << std::endl;
    std::cout << "x > y: " << maior << std::endl;
    std::cout << "x <= y: " << menor_igual << std::endl;

    return 0;
}