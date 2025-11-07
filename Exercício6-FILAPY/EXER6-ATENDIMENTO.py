import time
from collections import deque

def simular_fila():
    """
    Função principal que executa o menu e gerencia a fila de atendimento.
    """
    
    # Inicializa a fila. 'deque' é otimizado para operações 'append' (fim)
    # e 'popleft' (início), perfeito para FIFO.
    fila_de_atendimento = deque()

    print("--- Bem-vindo ao Sistema de Fila de Atendimento ---")

    while True:
        # Exibe o menu de opções
        print("\n" + "="*30)
        print("          MENU DE OPÇÕES")
        print("="*30)
        print("1 - Adicionar pessoa à fila")
        print("2 - Atender próxima pessoa")
        print("3 - Mostrar fila atual")
        print("4 - Sair")
        print("="*30)

        opcao = input("Escolha uma opção (1-4): ")

        # --- Opção 1: Adicionar Pessoa ---
        if opcao == '1':
            nome = input("Digite o nome da pessoa: ").strip() # .strip() remove espaços em branco
            if nome:
                fila_de_atendimento.append(nome)
                print(f"\n[SUCESSO] {nome} foi adicionado(a) ao final da fila.")
            else:
                print("\n[ERRO] O nome não pode ser vazio. Tente novamente.")

        # --- Opção 2: Atender Pessoa ---
        elif opcao == '2':
            # Verifica se a fila não está vazia
            if fila_de_atendimento:
                # 'popleft()' remove e retorna o PRIMEIRO item da fila (FIFO)
                pessoa_atendida = fila_de_atendimento.popleft()
                print(f"\n[ATENDIMENTO] {pessoa_atendida} está sendo atendido(a).")
            else:
                print("\n[INFO] A fila está vazia. Ninguém para atender.")

        # --- Opção 3: Mostrar Fila ---
        elif opcao == '3':
            if fila_de_atendimento:
                print("\n--- Fila de Espera Atual ---")
                print("(Primeiro a ser atendido -> Último)")
                # 'enumerate' é usado para numerar a fila, começando em 1
                for i, pessoa in enumerate(fila_de_atendimento, start=1):
                    print(f"{i}º: {pessoa}")
            else:
                print("\n[INFO] A fila está vazia.")

        # --- Opção 4: Sair ---
        elif opcao == '4':
            print("\nEncerrando o sistema. Até logo!")
            break # Quebra o loop 'while True' e encerra o programa

        # --- Opção Inválida ---
        else:
            print("\n[ERRO] Opção inválida. Por favor, digite um número de 1 a 4.")
        
        # Pequena pausa para o usuário ler a mensagem antes de mostrar o menu novamente
        time.sleep(1)

# Bloco de execução principal:
# Garante que a função simular_fila() só rode quando o script for executado diretamente
if __name__ == "__main__":
    simular_fila()