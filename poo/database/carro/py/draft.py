class Carro: 
    def __init__(self):
        self.passageiros: int = 0
        self.km: int = 0
        self.gas: int = 0

    def passMax(self, embarque: int) -> None:
        self.passageiros += embarque
        if self.passageiros > 2:
            self.passageiros = 2
            print("fail: limite de pessoas atingido")




