"""
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%

"""
aumento = 25
salario = float(input('Digite o seu salario: '))
salario_aumento = salario + (salario * (aumento / 100))

print(f'O se salario com aumento será R$ {salario_aumento}')
