# versão 1

c = float(input("Celsius: "))
f = (c * 9/5) + 32
print(f)

# versão 2

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Celsius: "))
print(celsius_para_fahrenheit(c))