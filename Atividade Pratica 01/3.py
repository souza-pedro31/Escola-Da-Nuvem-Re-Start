"""
3- Calculadora de Volume
* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.
"""

#Volume = Comprimento x Largura x Altura. 

print("--- BEM-VINDO(A) A CALCULADORA DE VOLUME ---")
comprimento = float(input("Entre com o valor do comprimento (cm): "))
largura = float(input("Entre com o valor da largura (cm): "))
altura = float(input("Entre com o valor da altura (cm): "))
volume = comprimento * largura * altura
print(f"O resultado do volume é {volume} cm³")