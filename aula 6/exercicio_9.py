# versão 1

texto = input()
contador = 0

for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1

print(contador)

# versão 2

def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

texto = input()
print(contar_vogais(texto))