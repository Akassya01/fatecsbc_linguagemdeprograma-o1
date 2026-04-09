# versão 1

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")
    
# versão 2

def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

a = int(input())
b = int(input())
c = int(input())
print(classificar_triangulo(a, b, c))