def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))
print(f"Fatorial de {numero}: {calcular_fatorial(numero)}")
