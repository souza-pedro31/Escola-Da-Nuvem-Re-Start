"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""

print("--- BEM-VINDO(A) AO VERIFICADOR DE SENHAS FORTES ---")

opcao = ""
while opcao != "sair":
    senha = input("Insira a senha: ")
    letra_maiuscula = False
    letra_minuscula = False
    caracter_especial = False
    quantidade_caracteres = 0
    tem_numero = False
    

    for s in senha:
        quantidade_caracteres += 1
        if s in ("abcdefghijklmnopqrstuvwxyz"):
            letra_minuscula = True
        elif s in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            letra_maiuscula = True
        elif s in ("!@#$%¨&*()[{]}"):
            caracter_especial = True
        elif s in ("1234567890"):
            tem_numero = True

    if quantidade_caracteres > 8 and letra_maiuscula and letra_minuscula and caracter_especial and tem_numero:
        print(f"A senha {'*'*quantidade_caracteres} é forte!")
    else:
        print(f"A senha {'*'*quantidade_caracteres} é fraca!")

    opcao = input("Deseja finalizar? digite \"sair\": ")
