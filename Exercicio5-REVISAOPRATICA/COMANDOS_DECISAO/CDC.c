#include <stdio.h>

int main() {
    int idade = 45;

    if (idade <= 12) {
        printf("Categoria: Crianca\n");
    } else if (idade <= 17) {
        printf("Categoria: Adolescente\n");
    } else if (idade < 60) {
        printf("Categoria: Adulto\n");
    } else {
        printf("Categoria: Idoso\n");
    }

    return 0;
}