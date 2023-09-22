"""Escreva um programa para fazer uma pesquisa de opinião sobre a
satisfação no atendimento de uma farmácia. As opções de respostas
devem ser INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER. O
algoritmo deverá ainda perguntar quantas usuários irão responder à
pergunta. Ao final apresentar o percentual de resposta de cada opção.
"""

# RESOLUÇÃO ABAIXO DA ATIVIDADE NO ENUNCIADO ACIMA, COM A ESTRUTURA DO WHILE ENVOLVIDA: 

# DFINIÇÃO DE UM MÉTODO COMO FUNÇÃO QUE IRÁ RECEBER UMA ESTRUTURA DE REPETIÇÃO: 

total_usuarios = int(input("Quantos usuários participarão da pesquisa: "))
insatisfeito = 0
satisafeito = 0
nao_qero_responder = 0

usuario_atual = 1

while usuario_atual <= total_usuarios:
    print(f"\nUsuário {usuario_atual}:")
    print(f"Opcao de resposta: ")
    print("1.INSAFISFEITO!")
    print("2.SATISFEITO!")
    print("3.NÃO QERO RESPONDER!")

    resposta = input("Escolha sua opção(1,2 ou 3): ")
# ESTRUTURA DE DECISÃO COM O IF PARA DEMONSTAR AS OPÇÕES DE ESCOLHA DE OPINIÃO PARA O USUÁRIO:
    if resposta == '1':
        insatisfeito += 1 
    elif resposta == '2':
        satisafeito += 1
    elif resposta == '3':
        nao_qero_responder += 1
    else: 
        print("Opção Inválida. Por favor, escolha uma opcao válida!")
    
    usuario_atual += 1

# DEMONSTAR NA TELA O RESULTADOS DE "VOTOS" EM FORMA PERCENTUAL A OPINIÃO DO PÚBLICO:

    print("\nResultados da pesquisa:")  
    print(f"Percentual de INSATISFEITO: \
            {insatisfeito / total_usuarios * 100:.2f}%") 
    print(f"Percentual de SATISFEITO:  \
            {satisafeito / total_usuarios * 100:.2f}%")
    print(f"Percentual de NÃO QERO RESPONDER: \
            {nao_qero_responder / total_usuarios * 100:.2f}%")



