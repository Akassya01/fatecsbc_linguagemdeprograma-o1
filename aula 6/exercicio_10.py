# versão 1

n = int(input())

for i in range(1, 11):
    print(n * i)
    
# versão 2

def gerar_tabuada(n):
    for i in range(1, 11):
        print(n * i)

n = int(input())
gerar_tabuada(n)