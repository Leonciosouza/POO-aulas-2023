""" Escreva uma função que receba dois conjuntos de números inteiros e
retorne um novo conjunto com os elementos que estão em ambos os
conjuntos. Por exemplo, se os conjuntos forem {1, 2, 3, 4} e {3, 4, 5, 6}, a
função deve retornar {3, 4}.
"""

# DEFINIÇÃO ABAIXO DOS 2 CONJUNTOS COM ALGUNS ELEMENTOS EM COMUM, COMO PEDIDO NO ENUNCIADO DA QUESTÃO ACIMA:

conj1 = {1, 2, 3, 4, 5, 6, 7}
conj2 = {3, 4, 5, 6, 8}

# DEFINIÇÃO ABAIXO DE UMA FUNÇÃO QUE IRÁ REALIZAR A INTERSECÇÃO DOS CONJUNTOS, USANDO O OPERADOR "&", E GERANDO UM NOVO CONJUNTO NO RETORNO:
def elementos_em_ambos_conj(conj1, conj2):
    interseccao = conj1 & conj2
    return interseccao

resultado = elementos_em_ambos_conj(conj1, conj2)
print(resultado)