from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def descricao(self):
        pass

class PratoPrincipal(Item):
    def descricao(self):
        return "Este é um prato principal."

class Sobremesa(Item):
    def descricao(self):
        return "Esta é uma sobremesa."

class CriadorDeItem(ABC):
    @abstractmethod
    def criar_item(self) -> Item:
        pass

class CriadorDePratoPrincipal(CriadorDeItem):
    def criar_item(self) -> Item:
        return PratoPrincipal()

class CriadorDeSobremesa(CriadorDeItem):
    def criar_item(self) -> Item:
        return Sobremesa()