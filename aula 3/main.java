import java.util.ArrayList;
import java.util.Scanner;

public class repeticao {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int num = 0;
        ArrayList<String> lista_de_produtos = new ArrayList<>();

        while (num != 3) {
            System.out.println("\nDigite um dos números abaixo:\n1-Adicionar\n2-Listar\n3-Sair\n");
            num = sc.nextInt();

            if (num == 1) {
                System.out.print("Digite o nome do produto: ");
                String nome_do_produto = sc.next();

                System.out.print("Digite a quantidade em estoque: ");
                int quantidade_em_estoque = sc.nextInt();

                System.out.print("Digite o preço unitário: ");
                double preco_unitario = sc.nextDouble();

                if (quantidade_em_estoque < 0) {
                    System.out.println("\nErro: quantidade negativa.");
                } else {
                    String produto = nome_do_produto + " " + quantidade_em_estoque + " " + preco_unitario;
                    lista_de_produtos.add(produto);
                    System.out.println("\nProduto cadastrado!");
                }
            }

            else if (num == 2) {
                for (int i = 0; i < lista_de_produtos.size(); i++) {
                    System.out.println("\nProduto " + (i+1) + ": " + lista_de_produtos.get(i));
                }
            }

            else if (num == 3) {
                break;
            }

            else {
                System.out.println("Opção inválida!");
            }
        }
    }
}