"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

print("--- BEM-VINDO(A) A CALCULADORA IMC ---")
peso = float(input("Insira seu peso (KG): "))
altura = float(input("Insira sua altura (M): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso")
elif imc < 25 and imc > 18.5:
    print(f"Seu IMC é {imc:.2f}, você está com o peso normal")
elif imc < 30 and imc > 25:
    print(f"Seu IMC é {imc:.2f}, você está sobrepeso")
else:
    print(f"Seu IMC é {imc:.2f}, você está obeso")
