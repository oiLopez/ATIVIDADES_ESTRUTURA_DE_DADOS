#include <iostream>

int main() {
    int numero;

    std::cout << "Digite um numero para ver a sua tabuada: ";
    
    std::cin >> numero;

    std::cout << "\n--- Tabuada do " << numero << " ---\n" << std::endl;


    for (int i = 1; i <= 10; ++i) {

        std::cout << numero << " x " << i << " = " << (numero * i) << std::endl;
    }

    return 0;
}