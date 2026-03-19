nome_do_produto = input("Digite o nome do produto: ")
quantidade_em_estoque = int(input("Digite a quantidade em estoque: "))
preco_unitario = float(input("Digite o preço unitário: "))

if quantidade_em_estoque > 0:
    print(f"\nResumo do produto cadastrado:\n \n nome: {nome_do_produto}\n quantidade em estoque: {quantidade_em_estoque} \n preço unitário: {preco_unitario}")
else:
    print(f"\nErro: a quantidade não pode ser um valor negativo.\nPor favor tente novamente.")