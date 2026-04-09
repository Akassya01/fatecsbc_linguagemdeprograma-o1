#versão 1 

n = int(input("Digite um número: "))

if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")
    
#versão 2

def verificar_paridade(n):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

n = int(input("Digite um número: "))
verificar_paridade(n)