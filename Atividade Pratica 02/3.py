"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

print("--- BEM-VINDO(A) A CALCULADORA DE MÉDIAS ---")

n1 = float(input("Insira a primeira nota: ").replace(',','.'))
n2 = float(input("Insira a segunda nota: ").replace(',','.'))
n3 = float(input("Insira a terceira nota: ").replace(',','.'))
print(f"As notas foram NOTA 1: {n1:.2f} | NOTA 2: {n2:.2f} | NOTA 3: {n3:.2f} | MÉDIA: {(n1 + n2 + n3)/3:.2f}")