# versão 1

valor = float(input("Valor: "))
desconto = float(input("Desconto (%): "))

final = valor - (valor * desconto/100)
print(final)

# versão 2

def aplicar_desconto(valor, desconto):
    return valor - (valor * desconto/100)

valor = float(input("Valor: "))
desconto = float(input("Desconto: "))
print(aplicar_desconto(valor, desconto))