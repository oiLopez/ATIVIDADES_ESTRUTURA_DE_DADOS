#include <stdio.h>

int main() {
    int numero = 7;
    int i;

    for (i = 1; i <= 10; i++) {
        int resultado = numero * i;
        printf("%d x %d = %d\n", numero, i, resultado);
    }

    return 0;
}