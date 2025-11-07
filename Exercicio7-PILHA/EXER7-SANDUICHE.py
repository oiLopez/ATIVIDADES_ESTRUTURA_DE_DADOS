sanduiche_pilha = []

def mostrar_menu():
    print("\n --- Montagem do Sanduíche (Pilha LIFO) --- ")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado (topo)")
    print("4 - Mostrar sanduíche (de baixo para cima)")
    print("5 - Finalizar pedido")
    print("--------------------------------------------------")

def adicionar_ingrediente(pilha):
    ingrediente = input("Digite o nome do ingrediente: ")
    pilha.append(ingrediente)
    print(f"'{ingrediente}' foi adicionado ao topo do sanduíche.")

def remover_ingrediente(pilha):
    """Remove o ingrediente do topo da pilha (LIFO)."""
    if not pilha: 
        print(" O sanduíche está vazio! Não há o que remover.")
    else:
        removido = pilha.pop()
        print(f"{removido}' foi removido do topo do sanduíche.")

def ver_topo(pilha):
    if not pilha:
        print("O sanduíche está vazio.")
    else:
        topo = pilha[-1]
        print(f" O último ingrediente adicionado (topo) é: '{topo}'")

def mostrar_sanduiche(pilha):
    if not pilha:
        print("O sanduíche está vazio.")
    else:
        print("\n--- Seu Sanduíche Completo ---")
        print("(Base)")
        for ingrediente in pilha:
            print(f" {ingrediente}")
        print("(Topo)")
        print("------------------------------")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            adicionar_ingrediente(sanduiche_pilha)
        
        elif opcao == '2':
            remover_ingrediente(sanduiche_pilha)
        
        elif opcao == '3':
            ver_topo(sanduiche_pilha)
        
        elif opcao == '4':
            mostrar_sanduiche(sanduiche_pilha)
        
        elif opcao == '5':
            print("\n Pedido finalizado! Bom apetite!")
            break 
        
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()