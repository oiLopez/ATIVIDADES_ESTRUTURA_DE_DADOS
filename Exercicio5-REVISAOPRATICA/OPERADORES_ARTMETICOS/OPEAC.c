#include <stdio.h>

int main() {
    int A = 15;
    int B = 4;
    
    int soma = A + B;
    int subtracao = A - B;
    int multiplicacao = A * B;
    int divisao_int = A / B;
    int modulo = A % B;
    
    float divisao_real = (float)A / B;

    printf("A + B = %d\n", soma);
    printf("A - B = %d\n", subtracao);
    printf("A * B = %d\n", multiplicacao);
    printf("A / B (Int) = %d\n", divisao_int);
    printf("A / B (Real) = %.2f\n", divisao_real);
    printf("A %% B = %d\n", modulo);

    return 0;
}