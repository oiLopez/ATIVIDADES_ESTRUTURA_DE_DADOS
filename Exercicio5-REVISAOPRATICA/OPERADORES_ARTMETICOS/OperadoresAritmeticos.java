public class OperadoresAritmeticos {
    public static void main(String[] args) {
        int A = 15;
        int B = 4;

        int soma = A + B;
        int subtracao = A - B;
        int multiplicacao = A * B;
        int divisao_int = A / B;
        int modulo = A % B;
        
        double divisao_real = (double)A / B;

        System.out.println("A + B = " + soma);
        System.out.println("A - B = " + subtracao);
        System.out.println("A * B = " + multiplicacao);
        System.out.println("A / B (Int) = " + divisao_int);
        System.out.printf("A / B (Real) = %.2f\n", divisao_real);
        System.out.println("A % B = " + modulo);
    }
}