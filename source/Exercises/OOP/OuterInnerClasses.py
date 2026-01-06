class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.itens = []
        self.Cliente = self.Cliente()

    class Cliente:
        def __init__(self, nome="", endereco="", email=""):
            self.nome = nome
            self.endereco = endereco
            self.email = email

    class Item:
        def __init__(self, nome, quantidade, preco_unitario):
            self.nome = nome
            self.quantidade = quantidade
            self.preco_unitario = preco_unitario

        def calcular_preco_total(self):
            return self.quantidade * self.preco_unitario

    def adicionar_item(self, nome, quantidade, preco_unitario):
        item = self.Item(nome, quantidade, preco_unitario)
        self.itens.append(item)

    def calcular_valor_total(self):
        return sum(item.calcular_preco_total() for item in self.itens)
    
    def __obter_detalhes_cliente(self):
        return f"Cliente: {self.Cliente.nome}, Endereço: {self.Cliente.endereco}, Email: {self.Cliente.email}"

    def __listar_itens(self):
        detalhes = []
        for item in self.itens:
            detalhes.append(f"Item: {item.nome}, Quantidade: {item.quantidade}, Preço Unitário: R$ {item.preco_unitario:.2f}, Preço Total: R$ {item.calcular_preco_total():.2f}")
        return detalhes
    
    def obter_resumo_pedido(self):
        resumo = self.__obter_detalhes_cliente() + "\nItens do Pedido:\n"
        resumo += "\n".join(self.__listar_itens())
        resumo += f"\nValor Total do Pedido: R$ {self.calcular_valor_total():.2f}"
        return resumo
    
# Exemplo de uso
pedido = Pedido(12345)
pedido.Cliente.nome = "João Silva"
pedido.Cliente.endereco = "Rua das Flores, 123"
pedido.Cliente.email = "joao.silva@outlook.com"
pedido.adicionar_item("Caneta", 10, 1.50)
pedido.adicionar_item("Caderno", 5, 12.00)
total = pedido.calcular_valor_total()
print(f"Valor total do pedido {pedido.numero_pedido}: R$ {total:.2f}")
print(pedido.obter_resumo_pedido())
