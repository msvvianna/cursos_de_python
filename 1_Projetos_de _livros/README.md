# Intensivo Python - Resumo

### Capitulo 1 ###
- instalação do Python

Windows
	- faça download do instalador de Python para Windows acessando http://python.org/downloads/
	- Certifique-se de marcar a opção Add Python to PATH (Adicionar Python ao PATH)

Linux
	- Python já está instalado na maioria dos computadores Linux
	

### Capitulo 2 ###

# Variaveis #

    - Toda variável armazena um valor, que é a informação associada a essa variável
	- Boas práticas na criação de variáveis:	
		- Podem conter apenas letras, numeros e underscores
		- Devem começar apenas com uma letra ou um underscore
		- Espaços não são permitidos
		- Evitar uso de palavras reservadas
		- Use nomes concisos, porém descritivos ("name é melhor que n")
		- Ter cuidado com uso do l minusculo e a letra O maiuscula, pois elas podem ser confundidas com 1 e 0
		- De preferencia sempre use letras minusculas como padrão

- Exemplos:

name = "ada lovelace"
print(name.title())  # coloca a primeira letra de cada palavra em maiuscula
print(name.lower())  # coloca as palavra em letra minuscula
print(name.upper())  # coloca as palavra em letra minuscula
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name  # concatenação
message = "Hello, " + full_name.title() + "!\n\n"
print(message)

- espaços e tabulações
print("Languages:\n\t- Python\n\t- C\n\t- Java")

- removendo espaços em brancos
favorite_language = ' python '
print(favorite_language)
favorite_language = favorite_language.rstrip()  # ' python' removemos os espaços extras do lado direito
print(favorite_language)
favorite_language = favorite_language.lstrip()  # 'python ' removemos os espaços extras do lado esquerdo
print(favorite_language)
favorite_language = favorite_language.strip()  # 'python' removemos os espaços extras de ambos lados
print(favorite_language)

- erros de sintaxe com strings
É quando o Python não reconhece uma seção de seu programa como um código Python válido

- devemos sempre alternar o uso de aspas simples com apostrofos ex: "''"

	message = "One of Phyton's strengths is its diverse community."
	print(message)
	
	
# Números Inteiros #

Você pode somar (+), subtrair (-), multiplicar (*) e dividir (/) inteiros em
Python.
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
>>> 3 ** 3
27
>>> 10 ** 6
1000000
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20

# Números de ponto flutuante (float) #

>>> 0.1
+ 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
- No entanto, tome cuidado, pois, às vezes, você poderá obter um
número arbitrário de casas decimais em sua resposta: 
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004

### Capitulo 3 ###

# Listas #

O que é uma lista?
Uma lista é uma coleção de itens em uma ordem em particular. Podemos
criar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os
nomes de todas as pessoas de sua família.


Listas são coleções ordenadas e é representada por colchete [] em Python






