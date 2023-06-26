from pymongo import MongoClient

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques



def listarPorDep():

    dep = input("[SISTEMA] Insira o departamento do(s) produto(s) que deseja checar.")
    produto = collection.find_one({"departamento": dep})

    if produto:
        print("====================== / CHECAR PRODUTO \ ======================\nID do Produto:", produto["idProduto"],"\nNome do produto:",produto["nomeProduto"] ,"\nQuantidade:", produto["quantidade"],"\nPreço:", produto["preco"],"\nFornecedor:", produto["fornecedor"],"\nDepartamento:", produto["departamento"],"\nCategoria:", produto["categoria"],"\n====================== / FIM CHECAR PRODUTO \ ======================")
    else:
        print("[ERRO]: Não foi possivel verificar o produto, verifique se foi adicionado o ID corredo ou se o produto existe.")
