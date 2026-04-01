#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> nomes;
    vector<int> quantidades;

    for (int i = 0; i < 3; i++) {
        string nome;
        int qtd;

        cout << "Digite o nome do produto: ";
        cin >> nome;

        cout << "Digite a quantidade: ";
        cin >> qtd;

        nomes.push_back(nome);
        quantidades.push_back(qtd);
    }

    cout << "\nRELATORIO FINAL:\n";

    for (int i = 0; i < 3; i++) {
        if (quantidades[i] < 5) {
            cout << "Produto: " << nomes[i] << " [REPOSICAO NECESSARIA] | Estoque: " << quantidades[i] << " unidades\n";
        } else {
            cout << "Produto: " << nomes[i] << " | Estoque: " << quantidades[i] << " unidades\n";
        }
    }

    return 0;
}