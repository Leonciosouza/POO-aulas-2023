"""Escreva um algoritmo que solicite ao usuário um número entre 1 e 10000 e
depois informe para o usuário se o número digitado é primo. Um número é dito
ser primo quando ele é divisível apenas por 1 e ele mesmo.
"""

# INCREMENTANDO UMA ESTRUTURA DE DECISÃO INICIALMENTE, UTILIZANDO DE OPERADORES RELACIONAIS: 

def verificar_primo(numero):

    if numero < 2:
        return False 
    if numero == 2:
        return True

# Verifica se o número é divisível por algum número até a raiz quadrada dele:

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True



# SOLICITA O NÚMERO AO USUÁRIO:

numero = int(input("Digite um número entre 1 e 10000: "))

# VERIFICAR SE O NÚMERO É PRIMO: 

if verificar_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")



