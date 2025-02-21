class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    
    def avaliar(self):
        if self.categoria == "eletrônicos":
            if self.preco > 100:
                return "Excelente"
            elif self.preco > 50:
                return "Bom"
            else:
                return "Regular"
        elif self.categoria == "roupas":
            if self.preco > 100:
                return "Bom"
            else:
                return "Regular"
        else:
            return "Desconhecida"

produto1 = Produto("Smartphone", 150, "eletrônicos")
produto2 = Produto("Fone de Ouvido", 40, "eletrônicos")
produto3 = Produto("Jaqueta", 120, "roupas")
produto4 = Produto("Camiseta", 30, "roupas")
produto5 = Produto("Livro", 25, "livros")

print(f"Avaliação do {produto1.nome}: {produto1.avaliar()}")
print(f"Avaliação do {produto2.nome}: {produto2.avaliar()}")
print(f"Avaliação do {produto3.nome}: {produto3.avaliar()}")
print(f"Avaliação do {produto4.nome}: {produto4.avaliar()}")
print(f"Avaliação do {produto5.nome}: {produto5.avaliar()}")
