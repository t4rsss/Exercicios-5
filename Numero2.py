def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número para verificar se é primo: "))
print(f"O número {numero} é primo? {eh_primo(numero)}")