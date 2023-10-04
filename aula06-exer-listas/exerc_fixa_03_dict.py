""" Escreva uma função que receba um dicionário que mapeia nomes de países
para suas populações e retorne o nome do país com a maior população. Por
exemplo, se o dicionário for {"Brasil": 211.8, "China": 1400.5, "Índia":
1366.4}, a função deve retornar "China". 
"""

# DEFINIÇÃO INICIAL DE UM DICIONÁRIO DE PARES DE CHAVES-VALORES: PAÍS E POPULAÇÃO RESPECTIVA:
paises_populacoes = {"Brasil": 211.8, "China": 1400.5, "índia": 1366.4, "Estados Unidos": 339.9, "Russia": 144.4, "Reino Unido": 67.7}


def retorna_pais_maior(paises_populacoes):
    if not paises_populacoes:
        return None
# Encontra o país com maior população com o uso da função max:     
    maior_pais = max(paises_populacoes, key= paises_populacoes.get)
    return maior_pais

# CHAMADA DA FUNÇÃO "Retorna_pais_maior", COM A PASSAGEM DE "paises_populacoes" COMO ARGUMENTO:
maior_pais = retorna_pais_maior(paises_populacoes)
print("País com maior quantidade de pessoas é:", maior_pais)


