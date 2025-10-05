import java.util.Locale;
import java.util.Scanner;

public class ATM {

    public static void main(String[] args) {
        

        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        

        double saldo = 2500.00;
        int opcao = 0;
        
        System.out.println("***************************************");
        System.out.println("Bem-vindo(a) ao Banco Digital!");
        System.out.printf("Saldo inicial: R$ %.2f\n", saldo);
        System.out.println("***************************************");

        do {
            System.out.println("\nEscolha uma operação:");
            System.out.println("1 - Consultar Saldo");
            System.out.println("2 - Depositar Valor");
            System.out.println("3 - Sacar Valor");
            System.out.println("4 - Sair");
            System.out.print(">> ");
            
            opcao = scanner.nextInt();
            

            switch (opcao) {
                case 1:
                    System.out.printf("Seu saldo atual é: R$ %.2f\n", saldo);
                    break;
                    
                case 2:
                    System.out.print("Digite o valor para depósito: R$ ");
                    double valorDeposito = scanner.nextDouble();
                    
                    if (valorDeposito > 0) {
                        saldo += valorDeposito; 
                        System.out.printf("Depósito realizado com sucesso! Novo saldo: R$ %.2f\n", saldo);
                    } else {
                        System.out.println("❌ Valor de depósito inválido!");
                    }
                    break;
                    
                case 3:
                    System.out.print("Digite o valor para saque: R$ ");
                    double valorSaque = scanner.nextDouble();
                    

                    if (valorSaque > saldo) {
                        System.out.println("❌ Saldo insuficiente!");
                    } else if (valorSaque <= 0) {
                        System.out.println("❌ Valor de saque inválido!");
                    } else {

                        saldo -= valorSaque; 
                        System.out.printf("Saque realizado com sucesso! Novo saldo: R$ %.2f\n", saldo);
                    }
                    break;
                    
                case 4:
                    System.out.println("Encerrando a sessão... Obrigado por usar nossos serviços!");
                    break;
                    
                default:
                    System.out.println("❌ Opção inválida! Por favor, escolha uma das opções do menu.");
            }
            
        } while (opcao != 4); 
        
        scanner.close();
    }
}