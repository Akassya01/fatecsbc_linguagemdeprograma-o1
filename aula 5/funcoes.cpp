#include <iostream>
#include <vector>
using namespace std;

string verificar_estoque_critico(int quantidade) {
    if (quantidade < 5) {
        return "[REPOSICAO NECESSARIA]";
    } else {
        return "";
    }
}

void exibir_cabecalho() {
    cout << "\n===== SORVETERIA DO DENER =====\n\n";
}

int main() {
    vector<string> nomes;
    vector<int> quantidades;

    for (int i = 0; i < 3; i++) {
        string nome;
        int qtd;

        cout << "Nome do produto: ";
        cin >> nome;

        cout << "Quantidade: ";
        cin >> qtd;

        nomes.push_back(nome);
        quantidades.push_back(qtd);
    }

    int num = 0;

    while (num != 2) {
        exibir_cabecalho();
        cout << "1 - Exibir relatorio\n2 - Sair\n";
        cin >> num;

        if (num == 1) {
            for (int i = 0; i < 3; i++) {
                string aviso = verificar_estoque_critico(quantidades[i]);
                cout << "Produto: " << nomes[i] << " " << aviso
                     << " | Estoque: " << quantidades[i] << endl;
            }
        }
    }

    return 0;
}