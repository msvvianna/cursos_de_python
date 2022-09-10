# Curso Completo de Python Geek University

- VARIAVEIS E TIPOS DE DADOS EM PYTHON

Real, Ponto futuante - float -> Numeros com casas decimais(2.56)

# errado do ponto de vista do float, mas gera uma tupla
valor1 = 1, 44
print(valor1)
print(type(valor1))

# certo do ponto de vista do float
valor2 = 1.44
print(valor2)
print(type(valor2))

# e possivel fazer dupla atribuição
valor3, valor4 = 1, 44
print(valor3)
print(type(valor3))
print(valor4)
print(type(valor4))

# podemos converter um float para um int
"""
obs: ao converter valores float para inteiros , nós perdemos a precisão.

"""
valor5 = 1.44
res = int(valor5)
print(res)
print(type(res))


# podemos trabalha com numeros complexos
variavel = 5j
print(variavel)
print(type(variavel))




