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

    def passMin(self, desembarque: int) -> None:
       self.passageiros-=desembarque 
       if self.passageiros < 0:
           self.passageiros = 0
           print("fail: nao ha ninguem no carro")

    def gasMax(self, tanque: int) -> None:
        self.gas += tanque
        if self.gas > 100:
            self.gas = 100
        
    def driveDistance(self) -> None:
        if self.gas< 0:
            self.gas = 0
            print("fail: tanque vazio")

        if self.passageiros < 0:
            self.passageiros = 0
            print("fail: nao ha ninguem no carro")

        if self.gas < self.km:
            self.gas = self.km 
            print("fail: tanque vazio após andar {km} km")


        def main ():
            carro: Carro = Carro("","")

            while True:
                line: str = input 
                print("$" + line)
                args: list[str] = line.split

                if args[0] == "end":
                    break 
                elif args[0] == "criar":
                    







