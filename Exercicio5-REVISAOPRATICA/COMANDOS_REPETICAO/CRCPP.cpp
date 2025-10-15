#include <iostream>

int main() {
    int numero = 5;

    for (int i = 1; i <= 10; i++) {
        int resultado = numero * i;
        std::cout << numero << " x " << i << " = " << resultado << std::endl;
    }

    return 0;
}