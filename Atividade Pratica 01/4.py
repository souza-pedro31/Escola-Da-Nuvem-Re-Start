"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

print("--- BEM-VINDO(A) A CALCULADORA DE PREÇO TOTAL ---")
nome_produto = str(input("Insira o nome do produto: ")).strip().upper()
preco_unitario = float(input("Insira o preço do produto (R$): ").replace(",","."))
quantidade_produto = int(input("Insira a quantidade do produto: "))
preco_total = preco_unitario * quantidade_produto
print(f"O preço total de {nome_produto} é R$ {preco_total:.2f}")