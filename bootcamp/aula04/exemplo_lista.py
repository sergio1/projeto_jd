produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list[str] = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() # remover o último item da lista
#produtos.remove(produto)

print(produtos)

numeros: list[int] = []
numeros.extend(range(0,5))
print(numeros)

produto_01: dict = { 
    "nome": "sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02: dict = { 
    "nome": "Televisao",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}
print(produto_01)

import json

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)
#print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)