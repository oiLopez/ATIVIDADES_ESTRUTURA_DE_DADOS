baralho_pilha = []

def mostrar_menu():
    print("\n--- Baralho de Cartas (Pilha LIFO) ---")
    print("1 - Adicionar carta (ao topo)")
    print("2 - Puxar carta (do topo)")
    print("3 - Ver carta do topo")
    print("4 - Mostrar baralho (de baixo para cima)")
    print("5 - Sair")
    print("------------------------------------------")

def adicionar_carta(pilha):
    carta = input("Digite o nome da carta (ex: 'Rei de Copas'): ")
    pilha.append(carta)
    print(f"'{carta}' foi adicionada ao topo do baralho.")

def puxar_carta(pilha):
    if not pilha:
        print("O baralho esta vazio! Nao ha cartas para puxar.")
    else:
        removida = pilha.pop()
        print(f"Voce puxou: '{removida}' (removida do topo).")

def ver_topo(pilha):
    if not pilha:
        print("O baralho esta vazio.")
    else:
        topo = pilha[-1]
        print(f"A carta no topo do baralho e: '{topo}'")

def mostrar_baralho(pilha):
    if not pilha:
        print("O baralho esta vazio.")
    else:
        print("\n--- Baralho Atual ---")
        print("(Base do baralho)")
        
        for carta in pilha:
            print(f" {carta}")
            
        print("(Topo do baralho)")
        print("-----------------------")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao (1-5): ")

        if opcao == '1':
            adicionar_carta(baralho_pilha)
        
        elif opcao == '2':
            puxar_carta(baralho_pilha)
        
        elif opcao == '3':
            ver_topo(baralho_pilha)
        
        elif opcao == '4':
            mostrar_baralho(baralho_pilha)
        
        elif opcao == '5':
            print("\nSaindo do programa. Ate mais!")
            break
        
        else:
            print("Opcao invalida. Por favor, escolha um numero de 1 a 5.")

if __name__ == "__main__":
    main()