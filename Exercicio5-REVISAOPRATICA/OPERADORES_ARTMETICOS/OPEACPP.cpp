#include <iostream>
#include <iomanip>

int main() {
    int A = 15;
    int B = 4;
    
    int soma = A + B;
    int subtracao = A - B;
    int multiplicacao = A * B;
    int divisao_int = A / B;
    int modulo = A % B;
    
    double divisao_real = (double)A / B;

    std::cout << "A + B = " << soma << std::endl;
    std::cout << "A - B = " << subtracao << std::endl;
    std::cout << "A * B = " << multiplicacao << std::endl;
    std::cout << "A / B (Int) = " << divisao_int << std::endl;
    std::cout << "A / B (Real) = " << std::fixed << std::setprecision(2) << divisao_real << std::endl;
    std::cout << "A % B = " << modulo << std::endl;

    return 0;
}