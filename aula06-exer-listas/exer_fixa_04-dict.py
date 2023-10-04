""" Escreva uma função que receba um dicionário que mapeia nomes de alunos
para suas notas e retorne um novo dicionário com os nomes dos alunos
aprovados e suas respectivas médias. Considere que um aluno é aprovado
se sua média for maior ou igual a 7. Por exemplo, se o dicionário for {"Ana":
[8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0]}, a função
deve retornar {"Ana": 8.33, "Carla": 8.0}.
"""

# RESOLUÇÃO DO ENUNCIADO DA QUESTÃO MENCIONADO ACIMA:

alunos_notas = {"Ana": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 4.0], "Carla": [7.0, 8.0, 9.0], "João": [5.5, 3.5, 6.5]}

# DEFINIÇÃO DE UMA FUNÇÃO QUE RECEBE EM SEGUIDA UM DICIONÁRIO PARA ARMAZENAR OS NOMES DOS ALUNOS APROVADOS E SUAS MÉDIAS:
def calcular_media_aluno(alunos_notas):
    alunos_aprovados = {}
    
# ITERAR SOBRE O DICIONÁRIO DE NOTAS DOS ALUNOS A SEREM APROVADOS:    
    for aluno, notas in alunos_notas.items():
        media = sum(notas) / len(notas)
# VERIFICAR SE O ALUNO FOI APROVADO (MÉDIA MAIOR OU IGUAL A 7.0):       
        if media >= 7.0:
            alunos_aprovados[aluno] = round(media, 2)
            
    return alunos_aprovados

# DEFINIÇÃO DE UM NOVO DICIONÁRIO COMO CHAMADA PARA A FUNÇÃO ACIMA DEFINIDA QUE JÁ ARMAZENA UM DICIONÁRIO COM NOMES E NOTAS RESPECTIVAS DOS ALUNOS:
alunos_aprovados = calcular_media_aluno(alunos_notas)
print(alunos_aprovados)
            