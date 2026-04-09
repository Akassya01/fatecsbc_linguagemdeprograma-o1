# versão 1

base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura
print(area)

# versão 2

def calcular_area_retangulo(base, altura):
    return base * altura

base = float(input("Base: "))
altura = float(input("Altura: "))
print(calcular_area_retangulo(base, altura))