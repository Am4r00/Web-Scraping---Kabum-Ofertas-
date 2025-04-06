# produto.py
# Essa classe serve para representar o que é um Produto que vamos buscar no site

class Produto:
    def __init__(self, nome, preco, parcela):
        self.nome = nome
        self.preco = preco
        self.parcela = parcela

    def __repr__(self):
        
        return f"Produto(nome={self.nome}, preco={self.preco}, parcela={self.parcela})"