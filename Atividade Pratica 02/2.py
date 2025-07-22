"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

print("--- BEM-VINDO(A) A CALCULADORA DE DESCONTO ---")
produto = input("Insira o nome do produto: ").upper().strip()
preco_produto = float(input("Insira o valor do produto: ").replace(',','.'))
desconto_produto = float(input("Insira o valor do desconto: ").replace(',','.'))

if desconto_produto > 100:
    desconto_produto = 100

preco_final = preco_produto - (preco_produto * (desconto_produto / 100))
print()
print(
f"Produto: {produto}\n\
Preço original: R$ {preco_produto:.2f}\n\
Desconto: {desconto_produto}%\n\
Valor final: R$ {preco_final:.2f}"
    )