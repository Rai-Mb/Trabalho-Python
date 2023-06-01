# 3. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Automóvel” e derive (Herança) as 4
# subclasses abaixo. Seu programa deve ter no mínimo 2 atributos e no mínimo 2 métodos (e garantir o Polimorfismo).

class Automovel:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        raise NotImplementedError('Método "acelerar" precisa ser implementado.')

    def frear(self):
        raise NotImplementedError('Método "frear" precisa ser implementado.')

class Carro(Automovel):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def acelerar(self):
        print('O carro está acelerando.')

    def frear(self):
        print('O carro está freando.')

class Caminhao(Automovel):
    def __init__(self, marca, modelo, pesoBrutoTotal):
        super().__init__(marca, modelo)
        self.pesoBrutoTotal = pesoBrutoTotal

    def acelerar(self):
        print('O caminhão está acelerando.')

    def frear(self):
        print('O caminhão está freando.')

class Caminhonete(Automovel):
    def __init__(self, marca, modelo, tracao4x4):
        super().__init__(marca, modelo)
        self.tracao4x4 = tracao4x4

    def acelerar(self):
        print('A caminhonete está acelerando.')

    def frear(self):
        print('A caminhonete está freando.')

class Moto(Automovel):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def acelerar(self):
        print('A moto está acelerando.')

    def frear(self):
        print('A moto está freando.')

carro1 = Carro('Fiat', 'Strada', 'marron')
caminhao1 = Caminhao('Volvo', 'FH', 430000)
caminhonete1 = Caminhonete('Chevrolet', 'S10', True)
moto1 = Moto('Honda', 'CBR', 650)

carro1.acelerar()
caminhao1.frear()
caminhonete1.frear()
moto1.acelerar()
