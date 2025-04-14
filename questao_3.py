from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def preparar(self):
        pass

class PratoPrincipal(ItemCardapio):
    def __init__(self):
        super().__init__("Prato Principal", 25.00)

    def preparar(self):
        return "Preparando o prato principal..."

class Sobremesa(ItemCardapio):
    def __init__(self):
        super().__init__("Sobremesa", 12.00)

    def preparar(self):
        return "Preparando a sobremesa..."

class CriadorDeItem(ABC):
    @abstractmethod
    def criar_item(self) -> ItemCardapio:
        pass

class CriadorDePratoPrincipal(CriadorDeItem):
    def criar_item(self) -> ItemCardapio:
        return PratoPrincipal()

class CriadorDeSobremesa(CriadorDeItem):
    def criar_item(self) -> ItemCardapio:
        return Sobremesa()

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: ItemCardapio):
        self.itens.append(item)

    def resumir_pedido(self):
        print("Resumo do Pedido:")
        for item in self.itens:
            print(f"- {item.nome}: R$ {item.preco:.2f} | {item.preparar()}")

if __name__ == "__main__":
    pedido = Pedido()

    fabrica_prato = CriadorDePratoPrincipal()
    pedido.adicionar_item(fabrica_prato.criar_item())

    fabrica_sobremesa = CriadorDeSobremesa()
    pedido.adicionar_item(fabrica_sobremesa.criar_item())

    pedido.resumir_pedido()






