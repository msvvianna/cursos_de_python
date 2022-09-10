"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais:
    - seu escopo compreende todo o programa
2 - Variaveis locais:
    - seu escopo esta limitado ao bloco onde ela foi declarada

Para declarar variavel em Python fazemos:
- nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica, ou seja não precisamos colocar o tipo de dado que a variavel pertence,
esse tipo de dado é inferido ao atribuirmos o valor a mesma
"""

number = 42  # Exemplo de variavel global
print(number)
print(type(number))
# saida 42 | <class 'int'>

words = 'Geek'
print(words)
print(type(words))
# saida Geek | <class 'str'>


number_two = 2
if number_two > 10:
    # new_number é um exemplo de variavel local, pois esta declarada no bloco if
    new_number = number_two + 10

print(new_number)
# saida -> NameError: name 'new_number' is not defined ()
