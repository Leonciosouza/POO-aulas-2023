"""Escreva uma função que receba uma tupla de números inteiros e retorne
uma nova tupla com os elementos pares da tupla original. Por exemplo, se a
tupla for (1, 2, 3, 4, 5), a função deve retornar (2, 4).
"""


#def retornar_pares():
#    pares = tuple(filter(lambda(x:x % 2 === 0,tupla))


#num_int_pares = (1, 2, 3, 4, 5)
#num_int_pares = [1, 2, 3, 4, 5]


#tupla = tuple(num_int_pares)

tupla_original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

def retorna_pares(tupla):
    num_pares = tuple(filter(lambda x:x % 2 == 0, tupla))
    return num_pares

pares_resultante = retorna_pares(tupla_original)
print(pares_resultante) # saída(2, 4).






