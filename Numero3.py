def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
print(f"Média dos números: {calcular_media(numeros)}")
