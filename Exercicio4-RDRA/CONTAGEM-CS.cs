using System;

class Program
{
    static void Main(string[] args)
    {

        int numero;


        Console.Write("Digite um numero inteiro positivo para iniciar a contagem regressiva: ");


        while (!int.TryParse(Console.ReadLine(), out numero) || numero < 0)
        {
            Console.WriteLine("Entrada invalida. Por favor, digite um numero inteiro positivo.");
            Console.Write("Digite um numero inteiro positivo para iniciar a contagem regressiva: ");
        }

        Console.WriteLine("\n--- Iniciando a contagem! ---\n");

        while (numero >= 0)
        {

            Console.WriteLine(numero);


            numero--; 
        }

        Console.WriteLine("\n--- Fim da contagem! ---");
    }
}