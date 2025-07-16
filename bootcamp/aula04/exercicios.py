# Crie um dicionário para armazenar informações de um livro,
# incluindo título, autor e ano de publicação.

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 2005
}

livro_02: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "George R. R. Martin",
    "Ano": 2007
}

lista_de_livros: list = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

#print(lista_de_livros)

lista_de_livros_usando_dict:dict = {
    "livro_01" : {
        "Titulo": "Game of Thrones",
        "Autor": "George R. R. Martin",
        "Ano": 2005
    },

    "livro_02" : {
        "Titulo": "Game of Thrones 2",
        "Autor": "George R. R. Martin",
        "Ano": 2007
    }
}

print(lista_de_livros_usando_dict["livro_01"])
print(lista_de_livros_usando_dict["livro_01"]["Titulo"])


# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros:list[int] = list(range(1,11))
for numero in numeros: 
    print(f"{numero} elevado ao quadrado [e {numero**2}])")

# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
linguagens: list[str] = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano_publicacao": 1949
}
print(f"Titulo: {livro['titulo']}")
print(f"Autor: {livro['autor']}")
print(f"Ano de Publicação: {livro['ano_publicacao']}")

# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
texto: str = "Sergio MMM"
ocorrencias: Dict[str, int] = {}
for char in texto: 
    if char in ocorrencias:
        ocorrencias[char] += 1
    else: 
        ocorrencias[char] = 1

print("Ocorrências de cada caractere: ", ocorrencias)


# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

# 6) Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

#7) Filtragem de Dados
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]
print(idades)
for idade in idades:
    if idade >= 18:
        print(f"Idade maior ou igual a 18: {idade}")

#8) Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)

# 9) Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print("Média:", media)


# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares: list[int] = []
impares: list[int] = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else: 
        impares.append(valor)

print("Pares:", pares)
print("Ímpares:", impares)


# 11) Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 100

print(produtos)

# 12) Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13) Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_positivo: dict = {}
for produto, quantidade in estoque.items():
    if quantidade > 0:
        estoque_positivo[produto] = quantidade

print(estoque_positivo)

# 14) Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15) Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)

