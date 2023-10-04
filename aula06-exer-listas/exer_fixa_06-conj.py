""" Escreva uma função que receba um conjunto de strings e retorne um novo
conjunto com as strings que são palíndromos. Um palíndromo é uma palavra
que é igual quando lida de trás para frente. Por exemplo, se o conjunto for
{"arara", "casa", "ovo", "radar"}, a função deve retornar {"arara", "ovo",
"radar"}.
"""


# CONJUNTO DE STRING DE PALAVRAS A SEREM LIDAS E RETORNADAS POR UMA FUNÇÃO A SER DEFINIDA: 
strings = {"arara", "casa", "ovo", "radar"}

# DEFINIÇÃO DE UMA FUNÇÃO QUE IRÁ ITERAR SSOBRE CADA PALAVRAS NO CONJUNTO E VERIFICA SE A PALAVRA É IGUAL À SUA VERSÃO INVERTIDA, 
# CASO FOR, ELEA SERÁ ADICIONADA AO CONJUNTO DE PALÍDROMOS: 

def retorna_string(conj_strings):
    panlindromos = set()
    for palavra in conj_strings:
        if palavra == palavra[::-1]:
            panlindromos.add(palavra)
    return panlindromos        
        
panlindromos_encontrados = retorna_string(strings)
print(panlindromos_encontrados)
