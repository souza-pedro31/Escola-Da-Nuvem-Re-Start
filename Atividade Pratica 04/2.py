"""
2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  
"""

print("--- BEM-VINDO(A) A CALCULADORA DE MÉDIAS DE NOTAS ---")

notas = []
opcao = ""
media = 0
while opcao != "fim":
    nota_nova = float(input("Insira a nota: ").replace(",","."))
    notas.append(nota_nova)
    media = 0
    for n in notas: 
        media += n
    media = media / len(notas)
    print(f"A média atual é: {media:.2f}")
    opcao = input("Para finalizar digite \"fim\": ")

print("OK, programa finalizado")
print(f"Sua média foi: {media:.2f}")
