import java.util.ArrayList;
import java.util.Scanner;

public class funcoes {

    public static String verificar_estoque_critico(int quantidade) {
        if (quantidade < 5) {
            return "[REPOSICAO NECESSARIA]";
        } else {
            return "";
        }
    }

    public static void exibir_cabecalho() {
        System.out.println("\n===== SORVETERIA DO DENER =====\n");
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<String> nomes = new ArrayList<>();
        ArrayList<Integer> quantidades = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            System.out.print("Nome do produto: ");
            String nome = sc.next();

            System.out.print("Quantidade: ");
            int qtd = sc.nextInt();

            nomes.add(nome);
            quantidades.add(qtd);
        }

        int num = 0;

        while (num != 2) {
            exibir_cabecalho();
            System.out.println("1 - Exibir relatorio\n2 - Sair");
            num = sc.nextInt();

            if (num == 1) {
                for (int i = 0; i < 3; i++) {
                    String aviso = verificar_estoque_critico(quantidades.get(i));
                    System.out.println("Produto: " + nomes.get(i) + " " + aviso +
                            " | Estoque: " + quantidades.get(i));
                }
            }
        }
    }
}