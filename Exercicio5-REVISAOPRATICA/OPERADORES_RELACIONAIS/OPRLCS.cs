using System;

public class OperadoresRelacionais
{
    public static void Main(string[] args)
    {
        int x = 25;
        int y = 30;

        bool igual = x == y;
        bool diferente = x != y;
        bool maior = x > y;
        bool menor_igual = x <= y;

        Console.WriteLine($"x == y: {igual}");
        Console.WriteLine($"x != y: {diferente}");
        Console.WriteLine($"x > y: {maior}");
        Console.WriteLine($"x <= y: {menor_igual}");
    }
}