""" Escreva uma função que receba uma tupla de strings e retorne uma nova
tupla com as strings ordenadas alfabeticamente e sem repetições. Por
exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), a
função deve retornar ("banana", "laranja", "maçã", "uva").
"""

# RESOLUÇÃO DA QUESTÃO LOGO ACIMA, UTILIZANDO DA ESTRUTURA DE TUPLAS: 



# a função "retorna_string", primeiro converte a tupla para um set(conjuntos) para remover as repetições da tupla original,
# Em seguida, ela ordena os elementos alfabeticamente e retorna a tupla resultante:

tupla_string = ("banana", "maça", "laranja", "banana", "uva", "pêra", "mamão", "pêra")
# Ordena a tupla, e remove as duplicadas usando um set: 
 
def retorna_string(tupla_string):
    nova_string = tuple(sorted(set(tupla_string)))
    return nova_string

nova_string = retorna_string(tupla_string)
print(nova_string)