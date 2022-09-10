# Curso Completo de Python Geek University

- VARIAVEIS E TIPOS DE DADOS EM PYTHON

"""
Tipo String

Em python um dado é considerado tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas dupla -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas tripla -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''0

name = 'Geek University'
print(name)
print(type(name))

name = "Gina's Bar"
print(name)
print(type(name))

name = 'Angelina \nJolie'
print(name)
print(type(name))

name = 'Geek University'
print(name.upper()) # transforma em maiusculo

name = 'Geek University'
print(name.lower()) # transforma em minusculo

name = 'Geek University'
print(name.split()) # transforma em lista de strings

print(name[0:4])  # Slice de string
# saida Geek

print(name[5:15])  # Slice de string
# saida University

print(name.split())
# saida ['Geek', 'University']

print(name.split()[0])
# saida ['Geek']

print(name.split()[1])
# saida ['University']

"""
# - Estiver entre aspas dupla -> """uma string""", """234""", """a""", """True""", """42.3"""

# ['G', 'e', 'e', 'k']
# [ 0,   1,   2,   3 ] -> Posições

name = 'Geek University'
# [::-1] começa do primeiro elemento(:) até o ultimo elemento(:) e inverta(-1)
print(name[::-1])

print(name.replace('e', 'E'))



