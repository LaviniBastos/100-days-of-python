class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.ligado = False

    def start(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo}: Carro ligado.")
        else:
            print(f"{self.modelo}: O carro já está ligado.")

    def stop(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.modelo}: Carro desligado.")
        else:
            print(f"{self.modelo}: O carro já está desligado.")


meu_carro = Carro("Fusca")
meu_carro.start()
meu_carro.start()
meu_carro.stop()
meu_carro.stop()