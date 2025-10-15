#include <stdio.h>
#include <stdbool.h>

int main() {
    int x = 30;
    int y = 30;

    bool igual = x == y;
    bool diferente = x != y;
    bool maior = x > y;
    bool menor_igual = x <= y;

    printf("x == y: %d\n", igual);
    printf("x != y: %d\n", diferente);
    printf("x > y: %d\n", maior);
    printf("x <= y: %d\n", menor_igual);

    return 0;
}