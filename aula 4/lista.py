nomes = []
quantidades = []

for i in range(3):
    nome = input("Digite o nome do produto: ")
    qtd = int(input("Digite a quantidade: "))
    
    nomes.append(nome)
    quantidades.append(qtd)

print("\nRELATÓRIO FINAL:")

for i in range(3):
    if quantidades[i] < 5:
        print(f"Produto: {nomes[i]} [REPOSIÇÃO NECESSÁRIA] | Estoque: {quantidades[i]} unidades")
    else:
        print(f"Produto: {nomes[i]} | Estoque: {quantidades[i]} unidades")