"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

print("--- BEM-VINDO(A) AO CONVERSOR DE TEMPERATURA ---")
temperatura = float(input("Insira a temperatura em graus celsius: "))
opcao = input("Deseja converter para Fahrenheit ou Kelvin? [F/K]: ")[0].strip().upper()

if opcao == "F":
    conversao = (temperatura * 1.8) + 32
    print(f"{temperatura}º em Fahrenheit é {conversao}º")
elif opcao == "K":
    conversao = (temperatura + 273.15)
    print(f"{temperatura}º em Kelvin é {conversao}º")
else:
    print("Opção inválida")