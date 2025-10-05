#include <stdio.h>
#include <string.h> 

int main() {

    char palavra[100];
 
    int contadorVogais = 0;

    printf("Digite uma palavra: ");
 
    fgets(palavra, sizeof(palavra), stdin);
    
    palavra[strcspn(palavra, "\n")] = 0;

    int tamanho = strlen(palavra);


    for (int i = 0; i < tamanho; i++) {
        char letra = palavra[i];
        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u' ||
            letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') 
        {
            contadorVogais++;
        }
    }
    printf("\nA palavra '%s' tem %d vogais.\n", palavra, contadorVogais);
    
    return 0; 
}