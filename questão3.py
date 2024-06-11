def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

base = 2
expoente = 5
resultado = potencia(base, expoente)
print(resultado)