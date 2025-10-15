using System;

public class ComandosRepeticao
{
    public static void Main(string[] args)
    {
        int numero = 8;

        for (int i = 1; i <= 10; i++)
        {
            int resultado = numero * i;
            Console.WriteLine($"{numero} x {i} = {resultado}");
        }
    }
}