"""O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial.
"""

# DEFINIÇÃO DE UMA FUNÇÃO QUE CALCULA O FATORIAL DO NÚMERO PASSADO COMO ARGUMENTO:

def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial 
    
# SOLICITAR QUE O USUÁRIO INSIRA UM NÚMERO E CHAMA A FUNÇÃO PARA CALCULAR EXIBIR O FATORIAL DESSE NÚMERO, USANDO O TESTE ABAIXO:      
try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    resul_fatorial = calcular_fatorial(numero)
    print(f'O fatorial de {numero} é: {resul_fatorial}')
except ValueError:
    print("Por favor, insira um número inteiro válido.")
