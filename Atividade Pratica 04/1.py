"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.    
"""

print("--- BEM-VINDO(A) A CALCULADORA ---")
op = ""

while op != "N":
    n1 = float(input("Insira o primeiro valor: ").replace(",","."))
    n2 = float(input("Insira o segundo valor: ").replace(",","."))
    operacao = input("OK, a operação será feita com {n1} e {n2}.\nInforme a operação que deseja realizar [ + | - | * | / ]: ").strip()[0]

    if operacao == "+":
        resultado = n1 + n2
        print(f"O resultado da sua operação é: {resultado}")
        op = input("Deseja continuar? [S/N]: ").upper()[0]
    elif operacao == "-":
        resultado = n1 - n2
        print(f"O resultado da sua operação é: {resultado}")
        op = input("Deseja continuar? [S/N]: ").upper()[0]
    elif operacao == "*":
        resultado = n1 * n2
        print(f"O resultado da sua operação é: {resultado}")
        op = input("Deseja continuar? [S/N]: ").upper()[0]
    elif operacao == "/":
        resultado = n1 / n2
        print(f"O resultado da sua operação é: {resultado}")
        op = input("Deseja continuar? [S/N]: ").upper()[0]
    else:
        print("Operação inválida")
