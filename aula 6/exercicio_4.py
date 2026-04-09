# versão 1

nome = input("Nome: ")
idade = int(input("Idade: "))

print(f"Olá {nome}, você tem {idade} anos")

# versão 2

def gerar_mensagem_boas_vindas(nome, idade):
    return f"Olá {nome}, você tem {idade} anos"

nome = input("Nome: ")
idade = int(input("Idade: "))
print(gerar_mensagem_boas_vindas(nome, idade))