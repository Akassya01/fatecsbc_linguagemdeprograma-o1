#include <iostream>
#include <string>  // Adicionado para std::string
using namespace std;

string Main(){
    string nome_do_produto;
    cout << "Digite o nome do produto: ";
    cin >> nome_do_produto;
    return nome_do_produto;  // Adicionado return
}

float MAIN(){
    float preco_unitario;
    cout << "Digite o preço do produto: ";
    cin >> preco_unitario;
    return preco_unitario;  // Adicionado return
}

int main(){
    string nome_do_produto = Main();  // Chamada da função e armazenamento do retorno
    float preco_unitario = MAIN();    // Chamada da função e armazenamento do retorno
    int quantidade;
    cout << "Digite a quantidade em estoque: ";
    cin >> quantidade;

    if (quantidade < 0){
        cout << "Erro: A quantidade não pode ser um valor negativo. Por favor tente novamente" << endl;
    } 
    else{
        cout << "Resumo do produto cadastrado: " << nome_do_produto << ", Preço unitário: R$ " << preco_unitario << ", Quantidade em estoque: " << quantidade << endl;
    }
    return 0;
}