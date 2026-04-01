#include <iostream>
#include <vector>
using namespace std;

int main() {
    int num = 0;
    vector<string> lista_de_produtos;

    while (num != 3) {
        cout << "\nDigite um dos números abaixo:\n1-Adicionar\n2-Listar\n3-Sair\n\n";
        cin >> num;

        if (num == 1) {
            string nome_do_produto;
            int quantidade_em_estoque;
            float preco_unitario;

            cout << "Digite o nome do produto: ";
            cin >> nome_do_produto;

            cout << "Digite a quantidade em estoque: ";
            cin >> quantidade_em_estoque;

            cout << "Digite o preço unitário: ";
            cin >> preco_unitario;

            if (quantidade_em_estoque < 0) {
                cout << "\nErro: quantidade negativa.\n";
            } else {
                string produto = nome_do_produto + " " + to_string(quantidade_em_estoque) + " " + to_string(preco_unitario);
                lista_de_produtos.push_back(produto);
                cout << "\nProduto cadastrado!\n";
            }
        }

        else if (num == 2) {
            for (int i = 0; i < lista_de_produtos.size(); i++) {
                cout << "\nProduto " << i+1 << ": " << lista_de_produtos[i] << endl;
            }
        }

        else if (num == 3) {
            break;
        }

        else {
            cout << "Opção inválida!\n";
        }
    }

    return 0;
}