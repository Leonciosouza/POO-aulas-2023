# ATIVIDADE PRÁTICA DE SALA DE AULA DO SLIDE-07 CONCEITOS E IMPLEMENTAÇÕES: 
""" 1. Considere a abstração de um objeto carro. Crie uma classe que
possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""

class Carro:
    modelo = "Creta Cabuloso"
    quant_portas = 4
    chassi = "GCF6184"
    ano = 2018
    cor = "Preto"
    potencia = "166cv"
    passageiros = 5

    def dizerModelo(self):
        modelo1 = "Santa Fé"
        print(f"O modelo para mais visitado é: {self.modelo}, mas o modelo vendido é o:{modelo1}")
    
    def abrirPortas(self):
        quant_portas1 = 2
        print(f"A quantidade ideal é: {self.quant_portas}, embora alguns queira com: {quant_portas1}")
    
    def usufrui_Pessoas(self):
        passageiros_frequentes = 3
        print(f"A quantidade de usuários máximos é: {self.passageiros}, no entanto no dia a dia são usados com {passageiros_frequentes}")


# Instanciando objetos criados e definidos na Classe Carro: 

c1 = Carro()

c1.dizerModelo()

c1.modelo = "Creta Cinza"

print(f"O modelo que maioria dos clientes procuram quando disponível, é o :{c1.modelo}")



c2 = Carro()
