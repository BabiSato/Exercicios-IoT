estoque = {
    "Celular": 10,
    "Notebook": 5,
    "Tablet": 0,
    "Fone de Ouvido": 20
}

def verificar_estoque(nome_produto):
    if nome_produto in estoque:
        if estoque[nome_produto] > 0:
            return f"Produto {nome_produto} disponível"
        else:
            return f"Produto {nome_produto} fora de estoque"
    else:
        return f"Produto {nome_produto} não encontrado no estoque"

def vender_produto(nome_produto, quantidade):
    if nome_produto in estoque:
        if estoque[nome_produto] >= quantidade:
            estoque[nome_produto] -= quantidade
            return f"Venda realizada com sucesso. Quantidade vendida: {quantidade}"
        else:
            return f"Estoque insuficiente para o produto {nome_produto}"
    else:
        return f"Produto {nome_produto} não encontrado no estoque"

for produto, quantidade in estoque.items():
    status = "disponível" if quantidade > 0 else "fora de estoque"
    print(f"Produto: {produto}, Status: {status}")

print(verificar_estoque("Celular"))
print(verificar_estoque("Tablet"))
print(vender_produto("Notebook", 3))
print(vender_produto("Fone de Ouvido", 25))
print(verificar_estoque("Fone de Ouvido"))