from pymongo import MongoClient
import datetime
import random


uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def stockAddition():
    from main import admMenu
    while True:

        get_prod_name = input("Qual é o nome do produto que deseja adicionar? ")
        get_quant_compra = input("Qual é a quantidade que o produto vai ter? ")
        get_quant_saldo = input("Informe o saldo do item no estoque: ")
        get_price = input("Insira o preço do produto: ")
        get_for = input("Insira o nome do fornecedor: ")
        get_dep = input("Insira o departamento do item (Uso e consumo, obsoletos, mercadoria para revenda,etc): ")
        get_cat = input("Insira a categoria do produto (roupas, acessórios, calçados, etc.): ")

        random_id = random.randint(2, 99999)

        add_estoque = {
            "idProduto": random_id,
            "nomeProduto": get_prod_name,
            "quantidade": int(get_quant_compra),
            "saldo": int(get_quant_saldo),
            "preco": get_price,
            "fornecedor": get_for,
            "data": datetime.datetime.now(tz=datetime.timezone.utc),
            "departamento": get_dep,
            "categoria": get_cat,
            }


        collection.insert_one(add_estoque)
        print("[✅ SUCESSO]: O produto", get_prod_name, "foi adicionado com sucesso.\n====================LOG DE INFORMAÇÕES====================\nNome do produto:", get_prod_name,"\nQuantidade:", get_quant_compra, "\nPreço: R$",get_price, "\nFornecedor:", get_for, "\n====================FIM DO LOG====================")
        admMenu()
        break
