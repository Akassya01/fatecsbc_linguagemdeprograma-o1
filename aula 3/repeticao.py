num = 0
lista_de_produtos = []

while num != 3:
    num = int(input("\nDigite um dos números abaixo para continuar:\n1-Adicionar novo produto \n2-Listar produtos \n3-Sair\n\n"))

    if num == 1:
        nome_do_produto = input("Digite o nome do produto: ") 
        quantidade_em_estoque = int(input("Digite a quantidade em estoque: "))
        preco_unitario = float(input("Digite o preço unitário: "))
        
        if quantidade_em_estoque < 0:
            print("\nErro: a quantidade não pode ser negativa.")
        else:
            lista_de_produtos.append((nome_do_produto, quantidade_em_estoque, preco_unitario))
            print("\nProduto cadastrado com sucesso!")

    elif num == 2:
        for i in range(len(lista_de_produtos)):
            print(f"\nProduto {i+1}:")
            print(f"Nome: {lista_de_produtos[i][0]}")
            print(f"Quantidade: {lista_de_produtos[i][1]}")
            print(f"Preço: {lista_de_produtos[i][2]}")

    elif num == 3:
        break

    else:
        print("Opção inválida!")