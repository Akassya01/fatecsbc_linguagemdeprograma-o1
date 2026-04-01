def verificar_estoque_critico(quantidade):
    if quantidade < 5:
        return "[REPOSIÇÃO NECESSÁRIA]"
    else:
        return ""

def exibir_cabecalho():
    print("\n===== SORVETERIA DO DENER =====\n")

nomes = []
quantidades = []

# cadastro de 3 produtos
for i in range(3):
    nome = input("Nome do produto: ")
    qtd = int(input("Quantidade: "))
    
    nomes.append(nome)
    quantidades.append(qtd)

# laço principal (while)
num = 0

while num != 2:
    exibir_cabecalho()
    print("1 - Exibir relatório")
    print("2 - Sair")
    
    num = int(input("Escolha: "))
    
    if num == 1:
        for i in range(3):
            aviso = verificar_estoque_critico(quantidades[i])
            print(f"Produto: {nomes[i]} {aviso} | Estoque: {quantidades[i]}")