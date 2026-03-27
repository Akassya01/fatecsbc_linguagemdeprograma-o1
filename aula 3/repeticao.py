num=0
produtos_cadastrados = 0
lista_de_produtos = []

while num != 3:
    num = int(input("\nDigite um dos números abaixo para continuar:\n1-Adicionar novo produto \n2-Listar produtos \n3-Sair\n\n"))
    if num == 1:
     nome_do_produto = input("Digite o nome do produto: ") 
     quantidade_em_estoque = int(input("Digite a quantidade em estoque: "))
     preco_unitario = float(input("Digite o preço unitário: "))
     produtos_cadastrados += 1
     lista_de_produtos.append((nome_do_produto, quantidade_em_estoque, preco_unitario))
     
     if quantidade_em_estoque < 0:
        print(f"\nErro: a quantidade não pode ser um valor negativo.\nPor favor tente novamente.")
     else:
         print(f"\nResumo do produto cadastrado:\n \n nome: {nome_do_produto}\n quantidade em estoque: {quantidade_em_estoque} \n preço unitário: {preco_unitario}")    
    elif num == 2:
        for i in range (len(lista_de_produtos)):
            print(f"\nProduto {i+1}:\n nome: {lista_de_produtos[i][0]}\n quantidade em estoque: {lista_de_produtos[i][1]} \n preço unitário: {lista_de_produtos[i][2]}")
    else:
     print("Opção inválida!")
