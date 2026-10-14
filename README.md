# GitHub-IA-Dio
Projeto de entrega Dio.me GitHub com I.A

2 - Repetindo Textos ✏️
Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

O que aprenderemos?

Manipulação de Strings (string)
Números Inteiros (int)
Múltiplas repetições
Entrada de dados
Aproveitar as sugestões do Github Copilot

3 - Operações Matemáticas Simples 📐
Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

O que aprenderemos?

Operações Matemáticas Básicas
Entrada de dados
Utilização eficiente do Github Copilot

4 - Verificando Números Pares e Ímpares 🧮
Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

O que aprenderemos?

Utilização de condicionais em Python (if, else) para realizar verificações.
Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar.
Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código.

5 - Calculando Média de Notas 📚
Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

O que aprenderemos?

Uso de variáveis para armazenar dados fornecidos pelo usuário.
Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores.
Prática na solicitação e manipulação de entrada do usuário.

6 - Verificando Palíndromos 🔄
Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

O que aprenderemos?

Manipulação de strings em Python, especialmente invertendo uma string.
Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.


---------------------------------------------------------------------------------------------

# Códigos criados no codespace auxiliados pela I.A


1- Concatenando dados:

primeiro_dado = input("Digite o primeiro dado: ")
segundo_dado = input("Digite o segundo dado: ")

dados_concatenados = primeiro_dado + segundo_dado

print("Dados concatenados:", dados_concatenados)

2- Repetindo textos
texto = input("Digite um texto: ")
repeticoes = int(input("Digite a quantidade de repetições: "))

print(texto * repeticoes)

3 - Verificando pares. 

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

4- Operações matemáticas
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero

print("Resultado da soma:", soma)

5- Calculando média de notas

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print("Média:", media)

6- Verificando palindromos

palavra = input("Digite uma palavra: ")

if palavra.lower() == palavra.lower()[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

  

---------------------------------------------------------------------------------------------



