class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, gelada=True):
        super().__init__(nome, preco)
        self.gelada = gelada

    def __str__(self):
        tipo = "Gelada" if self.gelada else "Natural"
        return f"{self.nome} ({tipo}) - R${self.preco:.2f}"

class CriadorBebida:
    @staticmethod
    def criar_bebida(nome, preco, gelada=True):
        return Bebida(nome, preco, gelada)

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def resumir_pedido(self):
        print("Resumo do Pedido:")
        for item in self.itens:
            print(f"- {item}")
        total = sum(item.preco for item in self.itens)
        print(f"Total: R${total:.2f}")

pedido = Pedido()
pedido.adicionar_item(ItemCardapio("Hambúrguer", 18.50))
pedido.adicionar_item(ItemCardapio("Batata Frita", 8.00))

bebida = CriadorBebida.criar_bebida("Refrigerante", 5.00, gelada=True)
pedido.adicionar_item(bebida)

pedido.resumir_pedido()
