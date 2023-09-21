"""ESCREVA UM PROGRAMA QUE LEIA DOIS VALORES QUE REPRESENTEM O INÍCIO E O FIM DE UM INTERVALO. 
O PROGRAMA DEVERÁ LER UM TERCEIRO VALOR DIGITADO E VERIFICAR SE ESTE TERCEIRO VALOR ESTÁ DENTRO DO INTERVALO OU FORA.
CASO ESTEJA FORA DO INTERVALO, DEVERÁ INFORMAR SE ESTÁ NA PARTE INFERIOR OU SUPERIOR DO INTERVALO.
"""

inicio = int(input("Digite o valor de início de um intervalo: "))
fim = int(input("Digite o valor de fim de um intervalo: "))

# LER UM TERCEIRO VALOR FORA DO INTERVALO:



terce_valor = int(input("Digite um terceiro valor para o intervalor: "))

# VERIFICAR SE O TERCEIRO VALOR SE ENCONTRA DENTRO DO INTERVALO: 
if terce_valor >= inicio and terce_valor <= fim:
    print(f"O {terce_valor} está dentrpo do intervalo {inicio}, {fim}")
else: 
     if terce_valor < inicio: 
        print(f"O {terce_valor} está fora do intervalo e é inferior ao {inicio}")
     else:
        print(f"O {terce_valor} está fora do intervalo e é superior ao {fim}")


