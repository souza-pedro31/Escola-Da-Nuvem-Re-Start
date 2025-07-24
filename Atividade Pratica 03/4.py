"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

print("--- BEM-VINDO(A) AO VERIFICADOR DE ANO BISSEXTO ---")
ano = int(input("Insira o ano a ser verificado: "))

if ano % 100 == 0:
    if ano % 400 == 0:
        print(f"{ano} é um ano bissexto")
    else:
        print(f"{ano} não é um ano bissexto")
elif ano % 4 == 0:
    print(f"{ano} é um ano bissexto")
else:
    print("Ano inválido")