import time
from collections import deque

def simular_fila():
    fila_carrossel = deque()
    
    print("--- BEM VINDE AO CCO ---")
    
    while True:
        # Exibe o menu de opções
        print("\n" + "="*30)
        print("MENU DE OPÇÕES")
        print("="*30)
        print("1 - Adicionar um trem ao carrossel")
        print("2 - Fazer a rota do trem")
        print("3 - Mostrar carrossel atual")
        print("4 - Sair")
        print("="*30)
    
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
                COD = input("Digite o COD do material rodante: ").strip()
                if COD:
                    fila_carrossel.append(COD)
                    print(f"\n[SUCESSO] {COD} foi adicionado(a) ao final do carrossel.")
                    
        elif opcao == '2':
                if fila_carrossel:
                    MR_CARROSSEL = fila_carrossel.popleft()
                    print(f"\n[EM ROTA] {MR_CARROSSEL} está com a rota estabelecida")
                else:
                    print("\n[INFO] O carrossel está vazio.")
                    
        elif opcao == '3':
                if fila_carrossel:
                    print("\n--- Ordem carrossel ---")
                    for i, COD in enumerate(fila_carrossel, start=1):
                        print(f"{i}º: {COD}")
                else:
                    print("\n[INFO] O carrossel está vazio")
                    
        elif opcao == '4':
                print("\nEncerrando o sistema. Até logo!")
                break
            
        else:
                print("\n[ERRO] Opção inválida...")
                
if __name__ == "__main__":simular_fila()

       