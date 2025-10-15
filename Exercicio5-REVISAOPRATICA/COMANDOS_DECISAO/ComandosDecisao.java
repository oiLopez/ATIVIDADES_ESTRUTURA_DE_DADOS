public class ComandosDecisao {
    public static void main(String[] args) {
        int idade = 45;

        if (idade <= 12) {
            System.out.println("Categoria: Crianca");
        } else if (idade <= 17) {
            System.out.println("Categoria: Adolescente");
        } else if (idade < 60) {
            System.out.println("Categoria: Adulto");
        } else {
            System.out.println("Categoria: Idoso");
        }
    }
}