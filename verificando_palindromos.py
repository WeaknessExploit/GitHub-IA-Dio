palavra = input("Digite uma palavra: ")

if palavra.lower() == palavra.lower()[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")