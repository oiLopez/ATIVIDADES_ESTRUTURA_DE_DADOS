#include <iostream>
#include <string>

int main() {
    int idade = 13;

    if (idade <= 12) {
        std::cout << "Categoria: Crianca" << std::endl;
    } else if (idade <= 17) {
        std::cout << "Categoria: Adolescente" << std::endl;
    } else if (idade < 60) {
        std::cout << "Categoria: Adulto" << std::endl;
    } else {
        std::cout << "Categoria: Idoso" << std::endl;
    }

    return 0;
}