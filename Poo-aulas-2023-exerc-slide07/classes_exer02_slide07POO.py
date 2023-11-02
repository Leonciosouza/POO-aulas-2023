
# EXERCÍCIO PRÁTICO DE SALA DE AULA DEM POO, DO SLIDE 07 - DEFINIÇÃO DE CLASSES, EXERCÍCIO 02: S

""" 2. Considere a abstração de um objeto cachorro. Crie uma classe
que possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""

# RESOLUÇÃO LOGO ABAIXO COM A DEFINIÇÃO DA CLASSE CACHORRO E SEUS ATRIBUTOS E MÉTODOS DEFINIDOS: 


class Animal: 
    def __init__(self, peso, nome, raça, cor):
        self._peso =  peso
        self._nome = nome 
        self._raça = raça
        self._cor = cor
        self._posicao = 0
    
    def moverse(self):
        self._posicao += 1


class Cachorro(Animal): # Herança
    def __init__(self, peso, nome, raça):
     # Chama o construtor da Superclasse:    
        super().__init__(peso, nome, raça, cor="Amarelo com Preto")
    
    def latir(self): 
        print("Au-au-au-au...")
        
    def __str__(self):
        return f"Cachorro: {self._nome}, \
        Peso:  {self._peso}, \
        Posição: {self._posicao}, \
        Raça: {self._raça}, \
        Cor: {self._cor}"
        
        
# Testando e instanciando as classes criadas logo acima: 

cachorro = Cachorro("Pluto", 4, "Rotwaller")

cachorro = Cachorro(f"30-40Kg", 6, "Pastor Alemão")
cachorro.moverse()
cachorro.latir()

print(cachorro)


