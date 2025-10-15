public class OperadoresRelacionais {
    public static void main(String[] args) {
        int x = 25;
        int y = 30;

        boolean igual = x == y;
        boolean diferente = x != y;
        boolean maior = x > y;
        boolean menor_igual = x <= y;

        System.out.println("x == y: " + igual);
        System.out.println("x != y: " + diferente);
        System.out.println("x > y: " + maior);
        System.out.println("x <= y: " + menor_igual);
    }
}