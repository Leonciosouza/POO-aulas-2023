"""O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial.
"""

# EXERCÍCIO DE FIXAÇÃO 01 - DE Nº 01 DO ASSUNTO DE ESTRUTURA DE REPETIÇÃO COM O USO DO WHILE: 

numero = int(input("O fatorial de: "))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
