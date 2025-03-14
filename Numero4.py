def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in palavra if letra in vogais)

palavra = input("Digite uma palavra: ")
print(f"Número de vogais na palavra: {contar_vogais(palavra)}")