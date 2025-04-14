from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def preparar(self):
        pass

class PratoPrincipal(ItemCardapio):
    def preparar(self):
        print(f"Preparando o prato principal: {self.nome} por R${self.preco:.2f}")
        print("Cozinhando os ingredientes principais, temperando e finalizando o prato!")

class Sobremesa(ItemCardapio):
    def preparar(self):
        print(f"Preparando a sobremesa: {self.nome} por R${self.preco:.2f}")
        print("Misturando os ingredientes doces, refrigerando ou assando conforme necessário.")

