"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

TAXA_DOLAR = 5.20
TAXA_EURO = 6.15

print("--- BEM-VINDO(A) A CALCULADORA DE CONVERSÃO DE MOEDA ---")
vlr_real = float(input("Quanto de reais você deseja converter?: ").replace(',','.'))
print(f"R$ {vlr_real:.2f} seriam USD {(vlr_real / TAXA_DOLAR):.2f} e EUR {(vlr_real / TAXA_EURO):.2f}")