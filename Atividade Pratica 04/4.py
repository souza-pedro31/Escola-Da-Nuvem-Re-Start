"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  
"""

print("--- BEM-VINDO(A) AO VERIFICADOR DE NÚMEROS PARES E ÍMPARES ---")

opcao = ""
pares = 0
impares = 0
while opcao != "fim":
    try:
        numero = int(input("Insira seu número: "))
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é par!")
        else:
            impares += 1
            print(f"{numero} é ímpar!")
    except ValueError:
        print("Entrada inválida")
    

    opcao = input("Deseja finalizar? Digite \"fim\": ").strip().lower()
print(f"Quantidade:\nPares: {pares}\nÍmpares: {impares}")
