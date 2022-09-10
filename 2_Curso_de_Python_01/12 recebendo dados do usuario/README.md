# Curso Completo de Python Geek University

"""
Aula 11 - recebendo dados do usuario

String eh tudo que estiver em:
- aspas (simples, duplas, simples triplas, duplas triplas)

"""
# Entrada de dados
nome = input("Qual seu nome? ")  # Input entrada de dados

# Exemplo print python 2.x
# print('Seja bem-vindo %s' % nome)

# Exemplo print python 3.x
# print('Seja bem-vindo {}'.format(nome))

# Exemplo print python 3.7 atual
print(f'Seja bem-vindo {nome}')
idade = input("Qual a sua idade? ")

# Processamento

# Saida de dados

# Exemplo print python 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo print python 3.x
# print('A {} tem {}'.format(nome, idade))

# Exemplo print python 3.7 atual
print(f'A {nome} tem {idade} anos.')
print(f'A {nome} nasceu no ano de {2022 - int(idade)}')





