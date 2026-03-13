import java.util.Scanner;

/**
 * @param args
 */
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Digite o nome do produto: ");
    String nome_do_produto = scanner.nextLine();

    System.out.print("Digite o preço do produto: ");
    float preco_unitario = scanner.nextFloat();

    System.out.print("Digite a quantidade em estoque: ");
    int quantidade_em_estoque = scanner.nextInt();

    if (quantidade_em_estoque < 0) {
        System.out.println("Erro: a quantidade não pode ser um valor negativo. Por favor tente novamente.");
    } else {
        System.out.printf("Resumo do produto cadastrado: %s, Preço: %.2f, Quantidade: %d", nome_do_produto, preco_unitario, quantidade_em_estoque);
    }
    
    scanner.close();
}