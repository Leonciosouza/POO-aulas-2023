class Pessoa: 
    nome = "Jonathan_leo"

    def dizerNome(self):
        nome1 = "coisa"
        print(f"Meu nome é {self.nome} e coisa é: {nome1}")

        return nome1

    def outroMetodo(self):
        print(f"{self.dizerNome()}")







# Instancia de um objeto Pessoa, o qual será referenciado por p1: 

p1 = Pessoa()

p2 = Pessoa()

p1.dizerNome()

p2.nome = "É doideira"

p2.dizerNome()

print("Id p1", id(p1), "Id p2:", id(p2))