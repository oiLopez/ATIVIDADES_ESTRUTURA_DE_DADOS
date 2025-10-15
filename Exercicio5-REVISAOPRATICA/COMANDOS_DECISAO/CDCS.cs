using System;

public class ComandosDecisao
{
    public static void Main(string[] args)
    {
        int idade = 15;

        if (idade <= 12)
        {
            Console.WriteLine("Categoria: Crianca");
        }
        else if (idade <= 17)
        {
            Console.WriteLine("Categoria: Adolescente");
        }
        else if (idade < 60)
        {
            Console.WriteLine("Categoria: Adulto");
        }
        else
        {
            Console.WriteLine("Categoria: Idoso");
        }
    }
}