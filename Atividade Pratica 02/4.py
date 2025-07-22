"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final 
arredondado para duas casas decimais.
"""

print("--- BEM-VINDO(A) A CALCULADORA DE CONSUMO DE COMBUSTÍVEL ---")
distancia_percorrida = int(input("Insira a distancia percorrida (KM): "))
combustivel_gasto = int(input("Insira a quantidade de combustivel gasto (L): "))
print(f"Se você percorreu {distancia_percorrida} km e consumiu {combustivel_gasto} litros de combustivel,\
seu consumo médio é {(distancia_percorrida / combustivel_gasto):.2f} quilometros por litro")