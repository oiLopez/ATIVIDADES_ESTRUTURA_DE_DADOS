using System;

public class OperadoresAritmeticos
{
    public static void Main(string[] args)
    {
        int A = 15;
        int B = 4;

        int soma = A + B;
        int subtracao = A - B;
        int multiplicacao = A * B;
        int divisao_int = A / B;
        int modulo = A % B;
        
        double divisao_real = (double)A / B;

        Console.WriteLine($"A + B = {soma}");
        Console.WriteLine($"A - B = {subtracao}");
        Console.WriteLine($"A * B = {multiplicacao}");
        Console.WriteLine($"A / B (Int) = {divisao_int}");
        Console.WriteLine($"A / B (Real) = {divisao_real:F2}");
        Console.WriteLine($"A % B = {modulo}");
    }
}